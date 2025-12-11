import os
from unittest.mock import patch

import pytest
from pydantic import ValidationError

from vetlog_buddy.config import Settings


@pytest.fixture
def mock_env_vars():
    with patch.dict(
        os.environ,
        {
            "DB_HOST": "localhost",
            "DB_NAME": "vetlog",
            "DB_USER": "vetlogUser",
            "DB_PASSWORD": "vetlogDB",
        },
    ):
        yield


def test_settings_loads_from_env(mock_env_vars):
    settings = Settings()
    assert settings.db_host == "localhost"
    assert settings.db_name == "vetlog"
    assert settings.db_user == "vetlogUser"
    assert settings.db_password == "vetlogDB"


@pytest.fixture
def clean_env():
    with patch.dict(os.environ, {}, clear=True):
        yield


def test_settings_missing_required_vars(clean_env):
    with pytest.raises(ValidationError):
        Settings(_env_file=None)
