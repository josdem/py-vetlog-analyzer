#  Copyright 2025 Jose Morales contact@josdem.io
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License

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
        pet = [PET_ID, PET_NAME, datetime.now(), PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 1)

    def test_generate_first_vaccination_records(self):
        two_months_ago = datetime.now() - timedelta(weeks=8, days=8)
        pet = [PET_ID, PET_NAME, two_months_ago, PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 2)

    def test_generate_annual_vaccination_records(self):
        four_months_ago = datetime.now() - timedelta(weeks=20, days=8)
        pet = [PET_ID, PET_NAME, four_months_ago, PET_TYPE]
        self.assertEqual(context.vaccinate(pet), 3)


if __name__ == "__main__":
    unittest.main()
