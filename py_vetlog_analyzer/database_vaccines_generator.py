from py_vetlog_analyzer.database_connector import Connector
from datetime import datetime


class VaccinesGenerator:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()

    def generateVaccines(pet):
        if(pet[3] != "DOG"):
            return pet
        now = datetime.now()
        weeks = (now - pet[2]).days / 7
        print("weeks", int(weeks))

        match int(weeks):
            case weeks if weeks in range(6, 9):
                print("Vaccine 1: DA2PP")
                print("Vaccine 2: Deworming")
            case weeks if weeks in range(10, 13):
                print("Vaccine 1: DA2PP")
                print("Vaccine 2: Deworming")
                print("Vaccine 4: Leptospirosis")
            case weeks if weeks in range(14, 16):
                print("Vaccine 1: DA2PP")
                print("Vaccine 2: Deworming")
                print("Vaccine 4: Leptospirosis")
                print("Vaccine 5: Rabies")
            case weeks if weeks >= 17:
                print("Vaccine 1: DA2PP")
                print("Vaccine 2: Deworming")
                print("Vaccine 4: Leptospirosis")
                print("Vaccine 5: Rabies")
                print("Vaccine 5: Canine Influenza")

        print("id", pet[0], "name:", pet[1], "birthdate:", pet[2], "type:", pet[3])
        return pet
