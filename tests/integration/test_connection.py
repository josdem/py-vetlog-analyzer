from sqlalchemy import text


def test_database_connection(db_session):
    """
    Basic connectivity test for MySQL.
    """
    result = db_session.execute(text("SELECT 1 AS test_value"))
    row = result.fetchone()

    assert row is not None
    assert row.test_value == 1


def test_database_table_operations(db_session):
    """
    Create table, insert, query, drop using MySQL-safe SQL.
    """
    # Create table (MySQL-friendly)
    db_session.execute(
        text("""
        CREATE TABLE IF NOT EXISTS test_customers (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE
        )
        """)
    )

    # Insert a row
    db_session.execute(
        text("""
        INSERT INTO test_customers (name, email)
        VALUES ('John Doe', 'john@example.com')
        """)
    )
    db_session.commit()

    # Fetch the row
    result = db_session.execute(
        text("""
        SELECT name, email FROM test_customers 
        WHERE email = 'john@example.com'
        """)
    )
    row = result.fetchone()

    assert row is not None
    assert row.name == "John Doe"
    assert row.email == "john@example.com"

    # Cleanup
    db_session.execute(text("DROP TABLE test_customers"))
    db_session.commit()


def test_database_transaction_rollback(db_session):
    """
    MySQL-compatible transaction + rollback test.
    """
    # Temporary table (works in MySQL)
    db_session.execute(
        text("""
        CREATE TEMPORARY TABLE temp_test (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            value_text TEXT
        )
        """)
    )
    db_session.commit()

    # Initial row
    db_session.execute(text("INSERT INTO temp_test (value_text) VALUES ('initial')"))
    db_session.commit()

    # Attempted insert + rollback
    try:
        db_session.execute(
            text("INSERT INTO temp_test (value_text) VALUES ('rollback_me')")
        )
        db_session.rollback()
    except Exception:
        db_session.rollback()

    # Only initial row should remain
    result = db_session.execute(text("SELECT COUNT(*) FROM temp_test"))
    count = result.fetchone()[0]
    assert count == 1

    # Validate content
    row = db_session.execute(text("SELECT value_text FROM temp_test")).fetchone()

    assert row.value_text == "initial"
