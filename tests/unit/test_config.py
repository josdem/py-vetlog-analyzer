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
from unittest.mock import patch

from vetlog_buddy.config import Settings


@patch.dict(
    "os.environ",
    {
        "DB_HOST": "localhost",
        "DB_NAME": "vetlog",
        "DB_USER": "vetlogUser",
        "DB_PASSWORD": "vetlogDB",
    },
)
def test_settings_loads_from_env():
    settings = Settings()
    assert settings.db_host == "localhost"
    assert settings.db_name == "vetlog"
    assert settings.db_user == "vetlogUser"
    assert settings.db_password == "vetlogDB"


@patch.dict(
    "os.environ",
    {
        "DB_HOST": "localhost",
        "DB_NAME": "vetlog",
        "DB_USER": "vetlogUser",
        "DB_PASSWORD": "vetlogDB",
    },
)
def test_database_url_property():
    settings = Settings()
    expected_url = "mysql://vetlogUser:vetlogDB@localhost/vetlog"
    assert settings.database_url == expected_url
