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

import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class Connector:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("VETLOG_USER"),
            password=os.getenv("VETLOG_PASSWORD"),
            database=os.getenv("DATABASE"),
        )

    def get_connector(self):
        return self.connection
