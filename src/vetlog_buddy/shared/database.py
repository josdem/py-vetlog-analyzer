#  Copyright 2025 Jose Morales contact@josdem.io
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License

from urllib.parse import quote_plus
from sqlmodel import Session, create_engine

from vetlog_buddy.shared.config import get_settings

settings = get_settings()

database_url: str = f"mysql+mysqlconnector://{quote_plus(settings.db_user)}:{quote_plus(settings.db_password)}@{settings.db_host}/{settings.db_name}"
engine = create_engine(database_url, echo=False, pool_pre_ping=True)


def get_session() -> Session:
    return Session(engine)
