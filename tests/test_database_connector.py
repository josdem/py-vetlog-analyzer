from unittest.mock import MagicMock
from python.database_connector import *
import unittest

class FixedTest(unittest.TestCase):
    def test_database_connector(self):
        connector = Connector()
        connection = MagicMock()
        connector.connection = connection
        assert connector.get_connector() == connection