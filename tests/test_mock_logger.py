from unittest.mock import MagicMock
from py_vetlog_analyzer.logger import Logger
import unittest


class FixedTest(unittest.TestCase):
    def test_create_logger(self):
        log = Logger("Logger Test")
        log.log = MagicMock()
        log.formatter = MagicMock()
        log.console_handler = MagicMock()

        log.info("Hello World!")

        log.log.info.assert_called_once_with("Hello World!")
