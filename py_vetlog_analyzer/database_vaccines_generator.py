from py_vetlog_analyzer.database_connector import Connector
from datetime import datetime


class VaccinesGenerator:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()

    def generateVaccines(pet):
        now = datetime.now()
        weeks = (now - pet[2]).days / 7
        print("weeks", int(weeks))

        match int(weeks):
            case 4:
                print("Vaccine 1: Parvovirus")
                print("Vaccine 2: Distemper")
                print("Vaccine 3: Hepatitis")
            case 6:
                print("Vaccine 1: Parvovirus")
                print("Vaccine 2: Distemper")
                print("Vaccine 3: Hepatitis")
                print("Vaccine 4: Leptospirosis")
            case 8:
                print("Vaccine 1: Parvovirus")
                print("Vaccine 2: Distemper")
                print("Vaccine 3: Hepatitis")
                print("Vaccine 4: Leptospirosis")
                print("Vaccine 5: Parainfluenza")
            case 10:
                print("Vaccine 1: Parvovirus")
                print("Vaccine 2: Distemper")
                print("Vaccine 3: Hepatitis")
                print("Vaccine 4: Leptospirosis")
                print("Vaccine 5: Parainfluenza")

        print("id", pet[0], "name:", pet[1], "birthdate:", pet[2], "type:", pet[3])
        return pet
