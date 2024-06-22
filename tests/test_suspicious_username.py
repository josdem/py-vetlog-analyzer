import unittest

from py_vetlog_analyzer.suspicious_username import is_suspicious_username

class FixedTest(unittest.TestCase):
    def test_detect_suspicious_username(self):
        self.assertTrue(is_suspicious_username("PvbGzTHuyk"))