import unittest

from py_vetlog_analyzer.database_generate_vaccines import VaccinesGenerator


class FixedTest(unittest.TestCase):
    def test_list_pets(self):
        self.assertGreater(VaccinesGenerator().listing_pets(), 0)

if __name__ == "__main__":
    unittest.main()