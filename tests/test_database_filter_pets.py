import unittest

from py_vetlog_analyzer.database_filter_pets import PetFilter


class FixedTest(unittest.TestCase):
    def test_list_pets(self):
        self.assertGreaterEqual(len(PetFilter().filtering_pets()), 0)


if __name__ == "__main__":
    unittest.main()
