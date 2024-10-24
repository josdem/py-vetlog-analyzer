from typing import Final
from datetime import datetime
import unittest

from py_vetlog_analyzer.database_vaccines_generator import VaccinesGenerator

PET_ID: Final[str] = "1"
PET_TYPE: Final[str] = "DOG"
PET_NAME: Final[str] = "Cremita"


class FixedTest(unittest.TestCase):
    def test_generate_no_vaccination_records(self):
        pet = [PET_ID, PET_NAME, datetime.now(), PET_TYPE]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 0)

    def test_generate_first_vaccination_records(self):
        pet = [PET_ID, PET_NAME, datetime(2024, 8, 23), PET_TYPE]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 2)

    def test_generate_second_vaccination_records(self):
        pet = [PET_ID, PET_NAME, datetime(2024, 8, 3), PET_TYPE]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 3)

    def test_generate_third_vaccination_records(self):
        pet = [PET_ID, PET_NAME, datetime(2024, 7, 3), PET_TYPE]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 4)

    def test_generate_annual_vaccination_records(self):
        pet = [PET_ID, PET_NAME, datetime(2022, 10, 18), PET_TYPE]
        self.assertEqual(VaccinesGenerator().generate_vaccines(pet), 5)


if __name__ == "__main__":
    unittest.main()
