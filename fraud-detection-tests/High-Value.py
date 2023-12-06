from pyhive import hive

def rule_high_value_transactions():
    # Establish connection to Hive
    conn = hive.Connection(host='localhost', port=10000, database='FinTech')
    cursor = conn.cursor()

    # Calculate the threshold value outside the main query
    threshold_query = "SELECT AVG(amount) * 1.5 FROM transactions"
    cursor.execute(threshold_query)
    threshold_value = cursor.fetchone()[0]

    # Create the potential_fraud_transactions table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS potential_fraud_transactionsa (
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
    """
    cursor.execute(create_table_query)

    # High-Value Transactions Rule with partition columns
    query = f"""
    INSERT INTO TABLE potential_fraud_transactionsa
    PARTITION (year=2023, month=11, day=29) -- Adjust these values based on your data
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
    WHERE amount > {threshold_value}
    """
    cursor.execute(query)

    # Commit and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    rule_high_value_transactions()
