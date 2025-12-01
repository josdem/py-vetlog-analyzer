import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.mysql import MySqlContainer


@pytest.fixture(scope="session")
def mysql_container():
    """Create MySQL container used for test session"""
    container = MySqlContainer("mysql:8.0", dialect="pymysql")
    container.start()
    # This never worked, but it was a pain to find the right way to do it.
    # wait_for_logs(container, ".*ready for connections.*")
    yield container
    container.stop()


@pytest.fixture(scope="session")
def db_engine(mysql_container):
    """Create SQLAlchemy engine using the container connection URL"""
    connection_url = mysql_container.get_connection_url()
    engine = create_engine(connection_url, future=True)

    yield engine
    engine.dispose()


@pytest.fixture(scope="function")
def db_session(db_engine):
    """Create a database session for individual tests"""
    Session = sessionmaker(bind=db_engine, future=True)
    session = Session()

    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
