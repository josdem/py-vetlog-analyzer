from py_vetlog_analyzer.database_connector import Connector
from py_vetlog_analyzer.database_vaccines_generator import VaccinesGenerator


class PetFilter:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()

    def filtering_pets(self):
        self.cursor.execute(
            "SELECT pet.id, pet.name, pet.birth_date, breed.type FROM pet, vaccination, breed WHERE breed.id = pet.breed_id and vaccination.pet_id = pet.id and vaccination.status='PENDING' GROUP BY pet.id;"
        )
        pets_vaccinated = self.cursor.fetchall()
        print("Vaccinated pets found: ", len(pets_vaccinated))
        self.cursor.execute(
            "SELECT pet.id, pet.name, pet.birth_date, breed.type FROM pet, breed WHERE breed.id = pet.breed_id;"
        )
        pets = self.cursor.fetchall()
        pets_waiting_for_vaccines = [n for n in pets if n not in pets_vaccinated]

        for row in pets_waiting_for_vaccines:
            VaccinesGenerator().generate_vaccines(row)

        print("Pets waiting for vaccines found: ", len(pets_waiting_for_vaccines))
        self.connection.close()
        return pets_waiting_for_vaccines
