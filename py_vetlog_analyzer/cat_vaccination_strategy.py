from typing import Final
from py_vetlog_analyzer.vaccination_strategy import VaccinationStrategy
from py_vetlog_analyzer.database_vaccines_generator import VaccinesGenerator
from py_vetlog_analyzer.logger import Logger
from datetime import datetime

TRICAT: Final[str] = "TRICAT"
TRICAT_BOOST: Final[str] = "TRICAT_BOOST"
FeLV: Final[str] = "FeLV"


class CatVaccinationStrategy(VaccinationStrategy):

    def __init__(self, connection):
        self.connection = connection
        self.logger = Logger("CatVaccinationStrategy")

    def generate_vaccines(self, pet):
        count = 0
        self.logger.info("Registering vaccination for pet: %s", pet[1])
        now = datetime.now()
        weeks = (now - pet[2]).days / 7
        self.logger.info("Pet is %d weeks old", int(weeks))

        def register_vaccination(name):
            self.logger.info("Generating %s vaccination", name)
            VaccinesGenerator(self.connection).register_vaccination(name, pet)

        match int(weeks):
            case weeks if weeks in range(0, 9):
                register_vaccination("Deworming")
                count = 1
            case weeks if weeks in range(9, 17):
                register_vaccination(TRICAT)
                register_vaccination("Deworming")
                register_vaccination(TRICAT_BOOST)
                register_vaccination(FeLV)
                register_vaccination("Rabies")
                count = 5
            case weeks if weeks >= 17:
                register_vaccination(TRICAT)
                register_vaccination("Deworming")
                register_vaccination("Rabies")
                count = 3
        return count
