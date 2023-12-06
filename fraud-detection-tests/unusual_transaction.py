from pyhive import hive
from datetime import datetime, timedelta

def rule_unusual_transaction_frequency():
    # Establish connection to Hive
    conn = hive.Connection(host='localhost', port=10000, database='FinTech')
    cursor = conn.cursor()

    # Create the unusual_transaction_frequency table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS unusual_transaction_frequenc (
        customer_id STRING,
        total_transactions INT,
        start_date STRING,
        end_date STRING
    )
    PARTITIONED BY (year INT, month INT, day INT)
    STORED AS ORC
    """
    cursor.execute(create_table_query)

    # Get the current date and time
    current_datetime = datetime.now()
    year, month, day = current_datetime.year, current_datetime.month, current_datetime.day

    # Set the time frame for unusual frequency detection (e.g., 1 hour)
    time_frame_hours = 1
    start_date = (current_datetime - timedelta(hours=time_frame_hours)).isoformat()

    # Unusual Transaction Frequency Rule with dynamic partition columns
    query = f"""
    INSERT INTO TABLE unusual_transaction_frequenc
    PARTITION (year={year}, month={month}, day={day})
    SELECT
        customer_id,
        COUNT(transaction_id) AS total_transactions,
        '{start_date}' AS start_date,
        '{current_datetime.isoformat()}' AS end_date
    FROM transactions
    WHERE date_time BETWEEN '{start_date}' AND '{current_datetime.isoformat()}'
    GROUP BY customer_id
    HAVING total_transactions > 10
    """
    cursor.execute(query)

    # Commit and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    rule_unusual_transaction_frequency()
