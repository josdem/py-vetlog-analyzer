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
