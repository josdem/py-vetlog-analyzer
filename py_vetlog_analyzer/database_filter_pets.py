from py_vetlog_analyzer.database_connector import Connector
from py_vetlog_analyzer.database_vaccines_generator import VaccinesGenerator


class PetFilter:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()

    def filtering_pets(self):
        self.cursor.execute(
            "select pet.id, pet.name, pet.birth_date from pet, vaccination where vaccination.pet_id = pet.id and vaccination.status='PENDING' group by pet.id"
        )
        pets_vaccinated = self.cursor.fetchall()
        print("Vaccinated pets found: ", len(pets_vaccinated))
        self.cursor.execute("select pet.id, pet.name, pet.birth_date from pet")
        pets = self.cursor.fetchall()
        print("Finding pets need vaccines")
        pets_waiting_for_vaccines = [n for n in pets if n not in pets_vaccinated]

        for row in pets_waiting_for_vaccines:
            VaccinesGenerator.generateVaccines(row)

        print("Pets waiting for vaccines found: ", len(pets_waiting_for_vaccines))
        self.connection.close()
        return pets_waiting_for_vaccines
