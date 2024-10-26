from abc import ABC, abstractmethod

class VaccinationStrategy(ABC):
    @abstractmethod
    def vaccinate(self, pet):
        return pet