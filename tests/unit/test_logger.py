import unittest
from unittest.mock import MagicMock

from vetlog_buddy.shared.logger import Logger

class TestLogger(unittest.TestCase):
    def test_create_logger(self):
        log = Logger("Logger Test")
        log.log = MagicMock()
        log.formatter = MagicMock()
        log.console_handler = MagicMock()

        log.info("Hello World!")

        log.log.info.assert_called_once_with("Hello World!")

if __name__ == "__main__":
    unittest.main()
