from py_vetlog_analyzer.database_connector import Connector

class VaccinesGenerator:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()

    def listing_pets(self):
        print("Finding alls pets with vaccines in PENDING status")
        self.cursor.execute("select pet.id, pet.name from pet, vaccination where vaccination.pet_id = pet.id and vaccination.status='PENDING' group by pet.id")
        result = self.cursor.fetchall()
        print("Pets found: ", len(result))
        self.cursor.execute("select pet.id, pet.name from pet")
        pets = self.cursor.fetchall()
        print("Total Pets: ", len(pets))
        print("Finding pets need vaccines")
        pets_waiting_for_vaccines = [n for n in pets if n not in result]
        for row in pets_waiting_for_vaccines:
            print(
                "id",
                row[0],
                "name:",
                row[1]
        )
        print("Suspicious users found: ", len(pets_waiting_for_vaccines))
        self.connection.close()
        return len(pets) - len(result)
