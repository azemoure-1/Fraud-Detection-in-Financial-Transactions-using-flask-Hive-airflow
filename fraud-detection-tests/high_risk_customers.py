from pyhive import hive

def rule_high_risk_customers():
    # Establish connection to Hive
    conn = hive.Connection(host='localhost', port=10000, database='FinTech')
    cursor = conn.cursor()

    # Create the high_risk_customers table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS high_risk_customers (
        customer_id STRING,
        credit_score INT,
        fraud_reports INT
    )
    STORED AS ORC
    """
    cursor.execute(create_table_query)

    # High-Risk Customers Rule
    query = """
    INSERT INTO TABLE high_risk_customers
    SELECT
        c.customer_id,
        e.credit_scores AS credit_score,
        e.fraud_reports AS fraud_reports
    FROM customers c
    JOIN externalData e ON c.customer_id = e.customer_id
    WHERE e.credit_scores < 500 OR e.fraud_reports > 3
    """
    cursor.execute(query)

    # Commit and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    rule_high_risk_customers()
