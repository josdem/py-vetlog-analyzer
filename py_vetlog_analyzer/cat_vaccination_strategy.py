from py_vetlog_analyzer.vaccination_strategy import VaccinationStrategy

class CatVaccinationStrategy(VaccinationStrategy):
    def vaccinate(self, pet):
        return pet