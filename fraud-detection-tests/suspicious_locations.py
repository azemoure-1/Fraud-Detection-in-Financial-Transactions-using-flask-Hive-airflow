from pyhive import hive
from datetime import datetime, timedelta

def rule_suspicious_locations():
    # Establish connection to Hive
    conn = hive.Connection(host='localhost', port=10000, database='FinTech')
    cursor = conn.cursor()

    # Create the suspicious_locations table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS suspicious_locations (
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

    # Suspicious Locations Rule with dynamic partition columns
    query = f"""
    INSERT INTO TABLE suspicious_locations
    PARTITION (year={year}, month={month}, day={day}, hour={hour})
    SELECT
        transaction_id,
        date_time,
        amount,
        currency,
        merchant_details,
        customer_id,
        transaction_type,
        location
    FROM transactions
    WHERE location NOT IN (
        SELECT location FROM customers
        WHERE customer_id = transactions.customer_id
    )
    """
    cursor.execute(query)

    # Commit and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    rule_suspicious_locations()
