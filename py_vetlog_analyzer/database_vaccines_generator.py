from py_vetlog_analyzer.database_connector import Connector
from datetime import datetime


class VaccinesGenerator:

    def generate_vaccines(self):
        pet = self
        if pet[3] != "DOG":
            return pet
        now = datetime.now()
        weeks = (now - pet[2]).days / 7
        print("weeks", int(weeks))

        def registerVaccination(name):
            connection = Connector().get_connector()
            cursor = connection.cursor()

            print("id", pet[0], "name:", pet[1], "birthdate:", pet[2], "type:", pet[3])

            cursor.execute(
                "INSERT INTO vaccination (pet_id, name, date, status) VALUES (%s, %s, %s, 'PENDING')",
                (pet[0], name, datetime.now()),
            )
            connection.commit()

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
