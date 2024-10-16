from py_vetlog_analyzer.database_filter import Filter
from unittest.mock import MagicMock
import unittest


class FixedTest(unittest.TestCase):
    def test_mock_filter(self):
        filter = Filter()
        filter.connection = MagicMock()
        filter.cursor = MagicMock()
        filter.filter_usernames()
        filter.cursor.execute.assert_called_with("SELECT * FROM user")
        filter.cursor.fetchall.assert_called_once()
        filter.connection.close.assert_called_once()
