import pytest

from vetlog_buddy.users.models import User
from vetlog_buddy.users.repository import UserRepository
from vetlog_buddy.users.services import UserService


class DummyRepo(UserRepository):
    def __init__(self):
        pass


"""
Note parametrize accepts any of these

    "username,expected"
    ("username", "expected")
    ["username", "expected"]

Linters seem to prefer tuple format
"""


@pytest.mark.parametrize(
    ("username", "expected"),
    [
        ("PvbGzTHuyk", True),
        ("otzUnBpWKQj", True),
        ("dfLybkwvMBrtWcY", True),
        ("qIiaPgOoH", True),
        ("simonhodgson3237@icloud.com", False),
    ],
)
def test_is_suspicious(username, expected):
    """Confirm UserService marks usernames correctly as suspicious"""
    # usernames from test_suspicious_username.py
    service = UserService(repo=DummyRepo())
    user = User(username=username)
    assert service.is_suspicious(user) == expected


@pytest.mark.parametrize(
    ("username", "expected"),
    [
        ("josdem", True),
        ("johndoe", True),
        ("IRIS", True),
        ("Max", True),
        ("Jc", True),
        ("NHUQfuLarRMDj", False),
        ("rJVyFMNsmXhPUvG", False),
        ("rVhBLNPSNIPE", False),
        ("SxeQsgXI", False),
        ("NDDmMAUftYXkxO", False),
        ("AbCdE", True),  # 5 chars - too short
        ("AbCdEf", False),  # 6 chars - valid minimum length
    ],
)
def test_is_invalid(username, expected):
    """Confirm UserService marks usernames correctly as invalid"""
    # usernames from test_filter_username.py
    service = UserService(repo=DummyRepo())
    user = User(username=username)
    assert service.is_invalid(user) == expected
