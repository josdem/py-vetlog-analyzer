"""
This file replaces the old unittest-based database_filter tests:
- test_database_filter.py
- test_mock_filter.py
"""

import pytest

from py_vetlog_analyzer.database_filter import Filter


@pytest.fixture
def mock_connector(mocker):
    conn = mocker.MagicMock()
    return conn


@pytest.fixture
def filter_with_mock(mock_connector):
    f = Filter()
    f.connection = mock_connector
    f.cursor = mock_connector.cursor
    return f


@pytest.mark.parametrize("user_id", [1, 12, 99])
def test_filter_users_calls_cursor(filter_with_mock, user_id):
    """Replaces old unittest cursor tests"""
    filter_with_mock.filter_users(user_id)
    filter_with_mock.cursor.execute.assert_called_with("SELECT * FROM user")
    filter_with_mock.cursor.fetchall.assert_called_once()
    filter_with_mock.connection.close.assert_called_once()


def test_suspicious_usernames(filter_with_mock):
    """Replaces old unittest suspicious username tests"""
    result = filter_with_mock.suspicious_usernames()
    assert result is not None
