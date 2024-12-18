from py_vetlog_analyzer.user_remover import Remover
from unittest.mock import MagicMock
import unittest


class FixedTest(unittest.TestCase):
    def test_mock_remover(self):
        db_filter = Remover(MagicMock())
        db_filter.cursor = MagicMock()
        db_filter.remove_user(2)
        db_filter.cursor.execute.assert_called_with(
            "DELETE FROM user WHERE id = %s", (2,)
        )
        db_filter.connection.commit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
