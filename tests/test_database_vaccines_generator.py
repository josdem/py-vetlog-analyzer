from typing import Final
import unittest
import datetime

from py_vetlog_analyzer.database_vaccines_generator import VaccinesGenerator

PET_TYPE: Final[str] = "DOG"
PET_NAME: Final[str] = "Cremita"


class FixedTest(unittest.TestCase):
    def test_generate_first_vaccination_records(self):
        pet = ["1", PET_NAME, datetime.datetime(2024, 8, 23), PET_TYPE]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 2)

    def test_generate_second_vaccination_records(self):
        pet = ["1", PET_NAME, datetime.datetime(2024, 8, 3), PET_TYPE]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 3)

    def test_generate_third_vaccination_records(self):
        pet = ["1", PET_NAME, datetime.datetime(2024, 7, 3), PET_TYPE]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 4)

    def test_generate_annual_vaccination_records(self):
        pet = ["1", PET_NAME, datetime.datetime(2022, 10, 18), PET_TYPE]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 5)


if __name__ == "__main__":
    unittest.main()
