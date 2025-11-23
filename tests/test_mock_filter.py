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

import unittest
from unittest.mock import MagicMock

from vetlog_buddy.database_filter import Filter


class FixedTest(unittest.TestCase):
    def test_mock_filter(self):
        db_filter = Filter()
        db_filter.connection = MagicMock()
        db_filter.cursor = MagicMock()
        db_filter.filter_users(12)
        db_filter.cursor.execute.assert_called_with("SELECT * FROM user")
        db_filter.cursor.fetchall.assert_called_once()
        db_filter.connection.close.assert_called_once()
