from dataclasses import dataclass
from .person import Person

@dataclass
class Student(Person):
    """
    TODO: Document

    @property decorator -> getters for class 
    @setter decorator -> setters for class
    """

    _institution: str
    _major : str

    @property
    def institution(self) -> str:
        return self._institution


    @property
    def major(self) -> str:
        return self._major


    @institution.setter
    def institution(self, institution: str) -> None:
        self._institution = institution


    @major.setter
    def major(self, major: str) -> None:
        self._major = major


    def talk(self) -> str:
        print(f'Hello! My name is {self._first_name} {self._last_name}, I am a student at {self.institution}, studying {self._major}')

    
    def calculate(self, *args):

        num_grades = len(args)
        final_grade = sum(args)/num_grades

        print(f'The final grade is: {final_grade}')
