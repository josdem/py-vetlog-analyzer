from abc import ABC, abstractmethod

class VaccinationStrategy(ABC):

    @abstractmethod
    def generate_vaccines(self, pet):
        pass