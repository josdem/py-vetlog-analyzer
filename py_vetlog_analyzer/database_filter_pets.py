from py_vetlog_analyzer.database_connector import Connector
from py_vetlog_analyzer.vaccination_context import Context
from py_vetlog_analyzer.dog_vaccination_strategy import DogVaccinationStrategy
from py_vetlog_analyzer.cat_vaccination_strategy import CatVaccinationStrategy
from py_vetlog_analyzer.logger import Logger


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
                context = Context(DogVaccinationStrategy())
                context.vaccinate(row)
            if row[3] == "CAT":
                context = Context(CatVaccinationStrategy())
                context.vaccinate(row)

        self.logger.info(
            "Pets waiting for vaccines found: %s", len(pets_waiting_for_vaccines)
        )
        self.connection.close()
        return pets_waiting_for_vaccines
