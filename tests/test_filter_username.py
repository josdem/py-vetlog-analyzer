import unittest
from py_vetlog_analyzer.filter_username import filter_username


class FixedTest(unittest.TestCase):
    def test_filter_usname(self):
        factor = 0.5
        self.assertTrue(filter_username("josdem", factor))
        self.assertTrue(filter_username("johndoe", factor))
        self.assertTrue(filter_username("IRIS", factor))
        self.assertTrue(filter_username("Max", factor))
        self.assertTrue(filter_username("Jc", factor))
        self.assertFalse(filter_username("NHUQfuLarRMDj", factor))
        self.assertFalse(filter_username("rJVyFMNsmXhPUvG", factor))
        self.assertFalse(filter_username("rVhBLNPSNIPE", factor))
        self.assertFalse(filter_username("SxeQsgXI", factor))
        self.assertFalse(filter_username("NDDmMAUftYXkxO", factor))


if __name__ == "__main__":
    unittest.main()
