from pyhive import hive
from datetime import datetime

def rule_blacklisted_merchants():
    # Establish connection to Hive
    conn = hive.Connection(host='localhost', port=10000, database='FinTech')
    cursor = conn.cursor()

    # Create the blacklisted_merchants_transactions table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS blacklisted_merchants_transactions (
        transaction_id STRING,
        date_time STRING,
        amount DOUBLE,
        currency STRING,
        merchant_details STRING,
        customer_id STRING,
        transaction_type STRING,
        location STRING
    )
    PARTITIONED BY (year INT, month INT, day INT, hour INT)
    STORED AS ORC
    """
    cursor.execute(create_table_query)

    # Get the current date and time
    current_datetime = datetime.now()
    year, month, day, hour = current_datetime.year, current_datetime.month, current_datetime.day, current_datetime.hour

    # Blacklisted Merchants Rule with dynamic partition columns
    query = f"""
    INSERT INTO TABLE blacklisted_merchants_transactions
    PARTITION (year={year}, month={month}, day={day}, hour={hour})
    SELECT
        t.transaction_id,
        t.date_time,
        t.amount,
        t.currency,
        t.merchant_details,
        t.customer_id,
        t.transaction_type,
        t.location
    FROM transactions t
    JOIN blacklist b ON t.merchant_details = b.merchant_name
    """
    cursor.execute(query)

    # Commit and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    rule_blacklisted_merchants()
