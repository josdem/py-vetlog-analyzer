from typing import Final
from datetime import datetime, timedelta
import unittest
from unittest.mock import MagicMock
from py_vetlog_analyzer.vaccination_context import Context
from py_vetlog_analyzer.dog_vaccination_strategy import DogVaccinationStrategy

PET_ID: Final[str] = "1"
PET_TYPE: Final[str] = "DOG"
PET_NAME: Final[str] = "Cremita"

context = Context(DogVaccinationStrategy(MagicMock()))


class FixedTest(unittest.TestCase):
    def test_generate_no_vaccination_records(self):
        pet = [PET_ID, PET_NAME, datetime.now(), PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 0)

    def test_generate_first_vaccination_week_six(self):
        two_months_ago = datetime.now() - timedelta(weeks=6, days=8)
        pet = [PET_ID, PET_NAME, two_months_ago, PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 5)

    def test_generate_first_vaccination_week_eleven(self):
        three_months_ago = datetime.now() - timedelta(weeks=11, days=4)
        pet = [PET_ID, PET_NAME, three_months_ago, PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 5)

    def test_generate_annual_vaccination_records(self):
        six_months_ago = datetime.now() - timedelta(weeks=20, days=8)
        pet = [PET_ID, PET_NAME, six_months_ago, PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 4)


if __name__ == "__main__":
    unittest.main()
