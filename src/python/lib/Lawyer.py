from dataclasses import dataclass
from .worker import Worker

@dataclass
class Lawyer(Worker):
    """
    TODO: Document

    @property decorator -> getters for class 
    @setter decorator -> setters for class
    """

    _law_firm: str

    @property
    def law_firm(self) -> str:
        return self._law_firm


    @law_firm.setter
    def law_firm(self, law_firm: str) -> None:
        self._law_firm = law_firm


    def talk(self) -> str:
        print(f'Hello! My name is {self._first_name} {self._last_name}, I am a lawyer that works {self.weekly_hours} a week at {self._law_firm} and I have a salary of {self._salary}.')