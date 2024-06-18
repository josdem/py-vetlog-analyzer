import unittest

from py_vetlog_analyzer.database_filter import *
from py_vetlog_analyzer.database_connector import *


class FixedTest(unittest.TestCase):
    def test_connect(self):
        self.assertIsNotNone(Connector().get_connector())
        self.assertTrue(Filter().filter_usernames() >= 0)


if __name__ == "__main__":
    unittest.main()
