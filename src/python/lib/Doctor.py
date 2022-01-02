from dataclasses import dataclass
from .worker import Worker

@dataclass
class Doctor(Worker):
    """
    TODO: Document

    @property decorator -> getters for class 
    @setter decorator -> setters for class
    """

    _type: str


    @property
    def type(self) -> str:
        return self._type


    @type.setter
    def type(self, type: str) -> None:
        self._type = type


    def talk(self) -> str:
        print(f'Hello! My name is {self._first_name} {self._last_name}, I am a {self._type} doctor that works {self.weekly_hours} a week and I have a salary of {self._salary}.')