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

from .cat_vaccination_strategy import CatVaccinationStrategy
from .database_connector import Connector
from .dog_vaccination_strategy import DogVaccinationStrategy
from .logger import Logger
from .vaccination_context import Context


class PetFilter:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()
        self.logger = Logger("PetFilter")

    def filtering_pets(self):
        self.cursor.execute(
            "SELECT pet.id, pet.name, pet.birth_date, breed.type FROM pet, vaccination, breed WHERE breed.id = pet.breed_id and vaccination.pet_id = pet.id and vaccination.status='PENDING' GROUP BY pet.id;"
        )
        pets_vaccinated = self.cursor.fetchall()
        self.logger.info("Vaccinated pets found: %s", len(pets_vaccinated))
        self.cursor.execute(
            "SELECT pet.id, pet.name, pet.birth_date, breed.type FROM pet, breed WHERE breed.id = pet.breed_id;"
        )
        pets = self.cursor.fetchall()
        pets_waiting_for_vaccines = [n for n in pets if n not in pets_vaccinated]

        for row in pets_waiting_for_vaccines:
            if row[3] == "DOG":
                context = Context(DogVaccinationStrategy(self.connection))
                context.vaccinate(row)
            if row[3] == "CAT":
                context = Context(CatVaccinationStrategy(self.connection))
                context.vaccinate(row)

        self.logger.info(
            "Pets waiting for vaccines found: %s", len(pets_waiting_for_vaccines)
        )
        self.connection.close()
        return pets_waiting_for_vaccines
