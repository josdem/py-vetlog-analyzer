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

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_name: str
    db_user: str
    db_password: str

    @property
    def database_url(self) -> str:
        return (
            f"mysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}"
        )
