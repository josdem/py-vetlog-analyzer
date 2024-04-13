import unittest

from python.database_connection import *

class FixedTest(unittest.TestCase):
    def test_connect(self):
        self.assertIsNotNone(connect())

if __name__ == '__main__':
    unittest.main()        
