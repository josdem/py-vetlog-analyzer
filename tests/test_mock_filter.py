from py_vetlog_analyzer.database_filter import Filter
from unittest.mock import MagicMock
import unittest


class FixedTest(unittest.TestCase):
    def test_mock_filter(self):
        db_filter = Filter()
        db_filter.connection = MagicMock()
        db_filter.cursor = MagicMock()
        db_filter.filter_usernames()
        db_filter.cursor.execute.assert_called_with("SELECT * FROM user")
        db_filter.cursor.fetchall.assert_called_once()
        db_filter.connection.close.assert_called_once()
