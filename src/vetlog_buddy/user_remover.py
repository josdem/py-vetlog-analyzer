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

from py_vetlog_analyzer.logger import Logger


class Remover:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.logger = Logger("Filter")

    def remove_user(self, id: int):
        self.logger.info("Deleting user with id: %d", id)
        self.cursor.execute("DELETE FROM user WHERE id = %s", (id,))
        self.connection.commit()
