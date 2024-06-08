import unittest

from python.database_filter import *
from python.database_connector import *


class FixedTest(unittest.TestCase):
    def test_connect(self):
        self.assertIsNotNone(Connector().get_connector())
        self.assertTrue(Filter().filter_usernames() >= 0)


if __name__ == "__main__":
    unittest.main()
