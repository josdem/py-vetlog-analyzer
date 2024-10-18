import unittest
import datetime

from py_vetlog_analyzer.database_vaccines_generator import VaccinesGenerator


class FixedTest(unittest.TestCase):
    def test_generate_first_vaccination_records(self):
        pet = ["1", "Cremita", datetime.datetime(2024, 8, 23), "DOG"]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 2)

    def test_generate_second_vaccination_records(self):
        pet = ["1", "Cremita", datetime.datetime(2024, 8, 3), "DOG"]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 3)

    def test_generate_third_vaccination_records(self):
        pet = ["1", "Cremita", datetime.datetime(2024, 7, 3), "DOG"]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 4)

    def test_generate_annual_vaccination_records(self):
        pet = ["1", "Cremita", datetime.datetime(2022, 10, 18), "DOG"]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 5)


if __name__ == "__main__":
    unittest.main()
