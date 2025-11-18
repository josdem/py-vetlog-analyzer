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

from py_vetlog_analyzer.database_filter_pets import PetFilter
from unittest.mock import MagicMock
from datetime import datetime
import unittest


class FixedTest(unittest.TestCase):

    def test_mock_filter_dog_pets(self):
        db_filter = PetFilter()
        db_filter.connection = MagicMock()
        db_filter.cursor = MagicMock()
        db_filter.filtering_pets()
        db_filter.cursor.execute(
            "SELECT pet.id, pet.name, pet.birth_date, breed.type FROM pet, breed WHERE breed.id = pet.breed_id;",
            return_value=[1, "Cremita", datetime.now(), "DOG"],
        )
        db_filter.connection.close.assert_called_once()

    def test_mock_filter_cat_pets(self):
        db_filter = PetFilter()
        db_filter.connection = MagicMock()
        db_filter.cursor = MagicMock()
        db_filter.filtering_pets()
        db_filter.cursor.execute(
            "SELECT pet.id, pet.name, pet.birth_date, breed.type FROM pet, breed WHERE breed.id = pet.breed_id;",
            return_value=[1, "Diluvina", datetime.now(), "CAT"],
        )
        db_filter.connection.close.assert_called_once()
