from py_vetlog_analyzer.database_connector import Connector


class VaccinesGenerator:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()

    def generateVaccines(pet):
        print("id", pet[0], "name:", pet[1], "birthdate:", pet[2], "type:", pet[3])
        return pet
