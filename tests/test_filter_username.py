import unittest
from py_vetlog_analyzer.filter_username import filter_username


class FixedTest(unittest.TestCase):
    def test_filter_usname(self):
        self.assertTrue(filter_username("josdem"))
        self.assertTrue(filter_username("johndoe"))
        self.assertFalse(filter_username("NHUQfuLarRMDj"))
        self.assertFalse(filter_username("rJVyFMNsmXhPUvG"))


if __name__ == "__main__":
    unittest.main()
