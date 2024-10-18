import unittest

from py_vetlog_analyzer.database_vaccines_generator import VaccinesGenerator


class FixedTest(unittest.TestCase):
    def test_list_pets(self):
        pet = [1, "Cremita", "2020-01-01", "DOG"]
        vaccinesGenerator = VaccinesGenerator()
        vaccinesGenerator.generate_vaccines(pet)


if __name__ == "__main__":
    unittest.main()