from py_vetlog_analyzer.vaccination_strategy import VaccinationStrategy

class Context:

    def __init__(self, vaccination_strategy: VaccinationStrategy):
        self.vaccination_strategy = vaccination_strategy
        
    def vaccinate(self, pet):
        self.vaccination_strategy.vaccinate(pet)