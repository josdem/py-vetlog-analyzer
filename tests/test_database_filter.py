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

from py_vetlog_analyzer.database_filter import Filter
from py_vetlog_analyzer.database_connector import Connector


class FixedTest(unittest.TestCase):
    def test_connect(self):
        self.assertIsNotNone(Connector().get_connector())
        self.assertGreaterEqual(Filter().filter_users(12), 0)
        self.assertGreaterEqual(Filter().suspicious_usernames(), 0)


if __name__ == "__main__":
    unittest.main()
