from py_vetlog_analyzer.database_connector import Connector

class VaccinesGenerator:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()

    def listing_pets(self):
        count = 0
        print("Finding alls pets with vaccines in PENDING status")
        self.cursor.execute("select pet.id, pet.name, vaccination.status from pet, vaccination where vaccination.pet_id = pet.id and vaccination.status='PENDING' group by pet.id")
        result = self.cursor.fetchall()
        print("Pets found: ", len(result))
        self.connection.close()
        return len(result)
