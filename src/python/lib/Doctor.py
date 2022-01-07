from dataclasses import dataclass
from typing import ClassVar
from .worker import Worker

@dataclass
class Doctor(Worker):
    """
    TODO: Document

    @property decorator -> getters for class 
    @setter decorator -> setters for class
    """

    _type: str
    _doctor_count : ClassVar[int] = 0


    def __post_init__(self):
        Doctor._person_count+=1
        Doctor._doctor_count+=1



    @property
    def type(self) -> str:
        return self._type


    @type.setter
    def type(self, type: str) -> None:
        self._type = type


    def talk(self) -> str:
        print(f'Hello! My name is {self._first_name} {self._last_name}, I am a {self._type} doctor that works {self.weekly_hours} a week and I have a salary of {self._salary}.')