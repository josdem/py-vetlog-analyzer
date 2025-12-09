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

from unittest.mock import MagicMock
import pytest

from vetlog_buddy.database_filter import Filter


@pytest.fixture
def mock_connector():
    return MagicMock()


@pytest.fixture
def filter_with_mock(mock_connector):
    f = Filter()
    f.connection = mock_connector
    f.cursor = mock_connector.cursor
    return f


@pytest.mark.parametrize("user_id", [1, 12, 99])
def test_filter_users_calls_cursor(filter_with_mock, user_id):
    """Replaces old unittest cursor tests"""
    filter_with_mock.filter_users(user_id)
    filter_with_mock.cursor.execute.assert_called_with("SELECT * FROM user")
    filter_with_mock.cursor.fetchall.assert_called_once()
    filter_with_mock.connection.close.assert_called_once()


def test_suspicious_usernames(filter_with_mock):
    """Replaces old unittest suspicious username tests"""
    result = filter_with_mock.suspicious_usernames()
    assert result is not None
