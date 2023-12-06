import requests
from datetime import datetime
from pyhive import hive

def extract_year_month_day(date_time_str):
    date_time = datetime.fromisoformat(date_time_str)
    return date_time.year, date_time.month, date_time.day

def load_transactions_to_hive():
    # Fetch data from the API
    api_url = "http://127.0.0.1:5000/api/transactions"
    response = requests.get(api_url)
    transactions_data = response.json()

    # Establish connection to Hive
    conn = hive.Connection(host='localhost', port=10000, database='FinTech')
    cursor = conn.cursor()

    # Create Hive table if not exists (replace placeholders with actual column names and data types)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id STRING,
            date_time STRING,
            amount DOUBLE,
            currency STRING,
            merchant_details STRING,
            customer_id STRING,
            transaction_type STRING,
            location STRING
        )
        PARTITIONED BY (year INT, month INT, day INT)
        STORED AS ORC
    ''')

    # Prepare a batch insert query
    batch_insert_query = '''
        INSERT INTO TABLE transactions PARTITION (year, month, day)
        VALUES {}
    '''

    # Prepare values for batch insert
    values = []
    for transaction in transactions_data:
        year, month, day = extract_year_month_day(transaction['date_time'])
        values.append(f"('{transaction['transaction_id']}', '{transaction['date_time']}', {transaction['amount']}, '{transaction['currency']}', '{transaction['merchant_details']}', '{transaction['customer_id']}', '{transaction['transaction_type']}', '{transaction['location']}', {year}, {month}, {day})")

    # Execute batch insert
    if values:
        values_str = ', '.join(values)
        insert_query = batch_insert_query.format(values_str)
        cursor.execute(insert_query)
    
    # Commit and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    load_transactions_to_hive()
