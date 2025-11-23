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

from vetlog_buddy.filter_username import filter_username


class FixedTest(unittest.TestCase):
    def test_filter_usname(self):
        factor = 0.5
        self.assertTrue(filter_username("josdem", factor))
        self.assertTrue(filter_username("johndoe", factor))
        self.assertTrue(filter_username("IRIS", factor))
        self.assertTrue(filter_username("Max", factor))
        self.assertTrue(filter_username("Jc", factor))
        self.assertFalse(filter_username("NHUQfuLarRMDj", factor))
        self.assertFalse(filter_username("rJVyFMNsmXhPUvG", factor))
        self.assertFalse(filter_username("rVhBLNPSNIPE", factor))
        self.assertFalse(filter_username("SxeQsgXI", factor))
        self.assertFalse(filter_username("NDDmMAUftYXkxO", factor))


if __name__ == "__main__":
    unittest.main()
