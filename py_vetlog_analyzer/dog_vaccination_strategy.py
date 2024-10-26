from py_vetlog_analyzer.vaccination_strategy import VaccinationStrategy
from py_vetlog_analyzer.logger import Logger
from datetime import datetime


class DogVaccinationStrategy(VaccinationStrategy):

    def __init__(self):
        self.logger = Logger("DogVaccinationStrategy")

    def generate_vaccines(self, pet):
        count = 0
        self.logger.info("Registering vaccination for pet: %s", pet[1])
        now = datetime.now()
        weeks = (now - pet[2]).days / 7
        self.logger.info("Pet is %d weeks old", int(weeks))

        def register_vaccination(name):
            self.logger.info("Generating %s vaccination", name)

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
