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

from vetlog_buddy.shared.database import get_session
from vetlog_buddy.users.repository import UserRepository
from vetlog_buddy.users.services import UserService

from . import __project__, __version__
from .database_filter_pets import PetFilter


def remove_invalid_users():
    """Remove invalid users"""
    with get_session() as session:
        repo = UserRepository(session)
        service = UserService(repo)
        service.remove_invalid()


def list_suspicious_users():
    """List suspicious users"""
    with get_session() as session:
        repo = UserRepository(session)
        service = UserService(repo)
        service.list_suspicious()


def vaccines():
    PetFilter().filtering_pets()


def version_check():
    """Print version info"""
    print(f"{__project__} version {__version__}")
