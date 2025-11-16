from typing import Final
from datetime import datetime, timedelta
import unittest
from unittest.mock import MagicMock
from py_vetlog_analyzer.vaccination_context import Context
from py_vetlog_analyzer.cat_vaccination_strategy import CatVaccinationStrategy

PET_ID: Final[str] = "2"
PET_TYPE: Final[str] = "CAT"
PET_NAME: Final[str] = "Diluvina"

context = Context(CatVaccinationStrategy(MagicMock()))


class FixedTest(unittest.TestCase):
    def test_generate_early_vaccination_records(self):
        """Test early vaccination (0-8 weeks): Deworming only"""
        pet = [PET_ID, PET_NAME, datetime.now(), PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 1)

    def test_generate_first_vaccination_records(self):
        """Test unified plan (9-16 weeks): 5 vaccines"""
        two_months_ago = datetime.now() - timedelta(weeks=8, days=8)
        pet = [PET_ID, PET_NAME, two_months_ago, PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 5)

    def test_generate_annual_vaccination_records(self):
        """Test adult plan (17+ weeks): 3 vaccines"""
        four_months_ago = datetime.now() - timedelta(weeks=20, days=8)
        pet = [PET_ID, PET_NAME, four_months_ago, PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 3)


if __name__ == "__main__":
    unittest.main()
