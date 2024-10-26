from py_vetlog_analyzer.vaccination_strategy import VaccinationStrategy
from py_vetlog_analyzer.database_connector import Connector
from py_vetlog_analyzer.logger import Logger
from datetime import datetime


class CatVaccinationStrategy(VaccinationStrategy):

    def __init__(self):
        self.logger = Logger("CatVaccinationStrategy")

    def generate_vaccines(self, pet):
        count = 0
        self.logger.info("Registering vaccination for pet: %s", pet[1])
        now = datetime.now()
        weeks = (now - pet[2]).days / 7
        self.logger.info("Pet is %d weeks old", int(weeks))

        def register_vaccination(name):
            self.logger.info("Generating %s vaccination", name)
            connection = Connector().get_connector()
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO vaccination (pet_id, name, date, status) VALUES (%s, %s, %s, 'PENDING')",
                (pet[0], name, datetime.now()),
            )
            connection.commit()

        match int(weeks):
            case weeks if weeks in range(8, 16):
                register_vaccination("FVRCP")
                register_vaccination("Deworming")
                count = 1
            case weeks if weeks >= 16:
                register_vaccination("FVRCP")
                register_vaccination("Deworming")
                register_vaccination("Rabies")
                count = 2
        return count
