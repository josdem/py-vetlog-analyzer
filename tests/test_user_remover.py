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

from vetlog_buddy.user_remover import Remover


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
