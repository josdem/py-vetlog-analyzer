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

import pytest

from vetlog_buddy.suspicious_username import is_suspicious_username


@pytest.mark.parametrize(
    "username,expected",
    [
        ("PvbGzTHuyk", True),
        ("otzUnBpWKQj", True),
        ("dfLybkwvMBrtWcY", True),
        ("qIiaPgOoH", True),
        ("simonhodgson3237@icloud.com", False),
    ],
)
def test_is_suspicious_username(username, expected):
    assert is_suspicious_username(username) == expected
