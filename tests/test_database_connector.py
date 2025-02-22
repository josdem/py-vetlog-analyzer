from unittest.mock import MagicMock
from py_vetlog_analyzer.database_connector import Connector
import unittest


class FixedTest(unittest.TestCase):
    def test_database_connector(self):
        connector = Connector()
        connection = MagicMock()
        connector.connection = connection
        assert connector.get_connector() == connection
