from typing import Final
from datetime import datetime
import unittest
from py_vetlog_analyzer.vaccination_context import Context
from py_vetlog_analyzer.cat_vaccination_strategy import CatVaccinationStrategy

PET_ID: Final[str] = "2"
PET_TYPE: Final[str] = "CAT"
PET_NAME: Final[str] = "Diluvina"

context = Context(CatVaccinationStrategy())


class FixedTest(unittest.TestCase):
    def test_generate_no_vaccination_records(self):
        pet = [PET_ID, PET_NAME, datetime.now(), PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 0)

    def test_generate_first_vaccination_records(self):
        pet = [PET_ID, PET_NAME, datetime(2024, 8, 23), PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 1)

    def test_generate_annual_vaccination_records(self):
        pet = [PET_ID, PET_NAME, datetime(2022, 10, 18), PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 2)


if __name__ == "__main__":
    unittest.main()
