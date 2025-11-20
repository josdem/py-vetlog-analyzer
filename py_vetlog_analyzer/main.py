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

from py_vetlog_analyzer.database_filter import Filter
from py_vetlog_analyzer.database_filter_pets import PetFilter


def flter_by_username():
    Filter().filter_users(10)


def flter_by_name():
    Filter().filter_users(11)


def flter_by_last_name():
    Filter().filter_users(12)


def suggest():
    Filter().suspicious_usernames()


def vaccines():
    PetFilter().filtering_pets()
