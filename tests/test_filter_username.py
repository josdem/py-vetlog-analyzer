import unittest
from py_vetlog_analyzer.filter_username import filter_username


class FixedTest(unittest.TestCase):
    def test_filter_usname(self):
        self.assertTrue(filter_username("josdem"))
        self.assertTrue(filter_username("johndoe"))
        self.assertTrue(filter_username("IRIS"))
        self.assertTrue(filter_username("Max"))
        self.assertTrue(filter_username("Jc"))
        self.assertFalse(filter_username("NHUQfuLarRMDj"))
        self.assertFalse(filter_username("rJVyFMNsmXhPUvG"))
        self.assertFalse(filter_username("rVhBLNPSNIPE"))
        self.assertFalse(filter_username("SxeQsgXI"))
        self.assertFalse(filter_username("NDDmMAUftYXkxO"))


if __name__ == "__main__":
    unittest.main()
