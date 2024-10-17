from py_vetlog_analyzer.database_filter_pets import PetFilter
from unittest.mock import MagicMock
import unittest


class FixedTest(unittest.TestCase):
    def test_mock_filter_pets(self):
        db_filter = PetFilter()
        db_filter.connection = MagicMock()
        db_filter.cursor = MagicMock()
        db_filter.filtering_pets()
        db_filter.cursor.execute.assert_called_with(
            "SELECT pet.id, pet.name, pet.birth_date, breed.type FROM pet, breed WHERE breed.id = pet.breed_id;"
        )
        db_filter.connection.close.assert_called_once()
