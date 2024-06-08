import unittest

from python.database_filter import *
from python.filter_username import *


class FixedTest(unittest.TestCase):
    def test_connect(self):
        self.assertIsNotNone(connect())
        self.assertTrue(filter_usernames() >= 0)


if __name__ == "__main__":
    unittest.main()
