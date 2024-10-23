from py_vetlog_analyzer.database_connector import Connector
from datetime import datetime


class VaccinesGenerator:

    def generate_vaccines(self, pet):
        count = 0
        if pet[3] != "DOG":
            return pet
        now = datetime.now()
        weeks = (now - pet[2]).days / 7
        print("weeks", int(weeks))

        def register_vaccination(name):
            connection = Connector().get_connector()
            cursor = connection.cursor()

            print("id", pet[0], "name:", pet[1], "birthdate:", pet[2], "type:", pet[3])

            cursor.execute(
                "INSERT INTO vaccination (pet_id, name, date, status) VALUES (%s, %s, %s, 'PENDING')",
                (pet[0], name, datetime.now()),
            )
            connection.commit()

        match int(weeks):
            case weeks if weeks in range(6, 10):
                register_vaccination("DA2PP")
                register_vaccination("Deworming")
                count = 2
            case weeks if weeks in range(10, 14):
                register_vaccination("DA2PP")
                register_vaccination("Deworming")
                register_vaccination("Leptospirosis")
                count = 3
            case weeks if weeks in range(14, 17):
                register_vaccination("DA2PP")
                register_vaccination("Deworming")
                register_vaccination("Leptospirosis")
                register_vaccination("Rabies")
                count = 4
            case weeks if weeks >= 17:
                register_vaccination("DA2PP")
                register_vaccination("Deworming")
                register_vaccination("Leptospirosis")
                register_vaccination("Rabies")
                register_vaccination("Canine Influenza")
                count = 5
        return count
