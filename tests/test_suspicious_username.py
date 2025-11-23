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

from vetlog_buddy.suspicious_username import is_suspicious_username


class FixedTest(unittest.TestCase):
    def test_detect_suspicious_username(self):
        self.assertTrue(is_suspicious_username("PvbGzTHuyk"))
        self.assertTrue(is_suspicious_username("otzUnBpWKQj"))
        self.assertTrue(is_suspicious_username("dfLybkwvMBrtWcY"))
        self.assertTrue(is_suspicious_username("qIiaPgOoH"))
        self.assertFalse(is_suspicious_username("simonhodgson3237@icloud.com"))
