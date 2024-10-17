from py_vetlog_analyzer.database_connector import Connector
from datetime import datetime


class VaccinesGenerator:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()

    def generateVaccines(pet):
        pet = pet
        if pet[3] != "DOG":
            return pet
        now = datetime.now()
        weeks = (now - pet[2]).days / 7
        print("weeks", int(weeks))

        def registerVaccination(name):
            print("Registering vaccination", name)
            print("id", pet[0], "name:", pet[1], "birthdate:", pet[2], "type:", pet[3])

        match int(weeks):
            case weeks if weeks in range(6, 9):
                registerVaccination("DA2PP")
                registerVaccination("Deworming")
            case weeks if weeks in range(10, 13):
                registerVaccination("DA2PP")
                registerVaccination("Deworming")
                registerVaccination("Leptospirosis")
            case weeks if weeks in range(14, 16):
                registerVaccination("DA2PP")
                registerVaccination("Deworming")
                registerVaccination("Leptospirosis")
                registerVaccination("Rabies")
            case weeks if weeks >= 17:
                registerVaccination("DA2PP")
                registerVaccination("Deworming")
                registerVaccination("Leptospirosis")
                registerVaccination("Rabies")
                registerVaccination("Canine Influenza")
