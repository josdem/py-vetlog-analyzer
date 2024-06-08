from python.database_filter import *
from unittest.mock import MagicMock
import unittest

class FixedTest(unittest.TestCase):
    def test_mock_filter(self):
      filter = Filter()
      filter.connection = MagicMock()
      filter.cursor = MagicMock()
      assert filter.cursor.execute.called_once_with("SELECT * FROM user")
      assert filter.cursor.fetchall.called_once()
      assert filter.connection.close.called_once()