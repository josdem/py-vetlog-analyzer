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

from typing import Final
from py_vetlog_analyzer.vaccination_strategy import VaccinationStrategy
from py_vetlog_analyzer.database_vaccines_generator import VaccinesGenerator
from py_vetlog_analyzer.logger import Logger
from datetime import datetime

C6CV: Final[str] = "C6CV"
DEWORMING: Final[str] = "Deworming"
RABIES: Final[str] = "Rabies"
PUPPY: Final[str] = "PUPPY"
C4CV: Final[str] = "C4CV"


class DogVaccinationStrategy(VaccinationStrategy):

    def __init__(self, connection):
        self.connection = connection
        self.logger = Logger("DogVaccinationStrategy")

    def generate_vaccines(self, pet):
        count = 0
        self.logger.info("Registering vaccination for pet: %s", pet[1])
        now = datetime.now()
        weeks = (now - pet[2]).days / 7
        self.logger.info("Pet is %d weeks old", int(weeks))

        def register_vaccination(name):
            self.logger.info("Generating %s vaccination", name)
            VaccinesGenerator(self.connection).register_vaccination(name, pet)

        match int(weeks):
            case weeks if weeks in range(0, 6):
                register_vaccination(DEWORMING)
                count = 1
            case weeks if weeks in range(6, 12):
                register_vaccination(PUPPY)
                register_vaccination(C4CV)
                register_vaccination(C6CV)
                register_vaccination(DEWORMING)
                register_vaccination(RABIES)
                count = 5
            case weeks if weeks >= 12:
                register_vaccination(C6CV)
                register_vaccination(DEWORMING)
                register_vaccination(RABIES)
                count = 3
        return count
