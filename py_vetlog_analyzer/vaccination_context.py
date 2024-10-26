from py_vetlog_analyzer.vaccination_strategy import VaccinationStrategy


class Context:

    def __init__(self, vaccination_strategy: VaccinationStrategy):
        self.vaccination_strategy = vaccination_strategy

    def vaccinate(self, pet):
        return self.vaccination_strategy.generate_vaccines(pet)
