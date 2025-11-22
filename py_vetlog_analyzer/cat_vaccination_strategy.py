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


from py_vetlog_analyzer.vaccination_strategy import VaccinationStrategy
from py_vetlog_analyzer.database_vaccines_generator import VaccinesGenerator
from py_vetlog_analyzer.logger import Logger
from py_vetlog_analyzer.vaccine import Vaccine
from datetime import datetime


class CatVaccinationStrategy(VaccinationStrategy):

    def __init__(self, connection):
        self.connection = connection
        self.logger = Logger("CatVaccinationStrategy")

    def generate_vaccines(self, pet):
        count = 0
        self.logger.info("Registering vaccination for pet: %s", pet[1])
        now = datetime.now()
        weeks = (now - pet[2]).days / 7
        self.logger.info("Pet is %d weeks old", int(weeks))

        def register_vaccination(vaccine: Vaccine):
            self.logger.info("Generating %s vaccination", vaccine)
            VaccinesGenerator(self.connection).register_vaccination(vaccine, pet)

        match int(weeks):
            case weeks if weeks in range(0, 9):
                register_vaccination(Vaccine.DEWORMING)
                count = 1
            case weeks if weeks in range(9, 17):
                register_vaccination(Vaccine.TRICAT)
                register_vaccination(Vaccine.DEWORMING)
                register_vaccination(Vaccine.TRICAT_BOOST)
                register_vaccination(Vaccine.FeLV)
                register_vaccination(Vaccine.RABIES)
                count = 5
            case weeks if weeks >= 17:
                register_vaccination(Vaccine.TRICAT)
                register_vaccination(Vaccine.DEWORMING)
                register_vaccination(Vaccine.RABIES)
                count = 3
        return count
