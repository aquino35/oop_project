from dataclasses import dataclass
from .person import Person

@dataclass
class Worker(Person):
    """
    TODO: Document

    @property decorator -> getters for class 
    @setter decorator -> setters for class
    """

    _weekly_hours: int
    _salary : int

    @property
    def weekly_hours(self) -> int:
        return self._weekly_hours


    @property
    def salary(self) -> int:
        return self._salary


    @weekly_hours.setter
    def weekly_hours(self, weekly_hours: int) -> None:
        self._weekly_hours = weekly_hours


    @salary.setter
    def salary(self, salary: int) -> None:
        self._salary = salary


    def talk(self) -> str:
        print(f'Hello! My name is {self._first_name} {self._last_name}, I am a worker that works {self.weekly_hours} a week and I have a salary of {self._salary}')