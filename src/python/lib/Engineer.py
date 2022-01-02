from dataclasses import dataclass
from .worker import Worker

@dataclass
class Engineer(Worker):
    """
    TODO: Document

    @property decorator -> getters for class 
    @setter decorator -> setters for class
    """

    _type: str
    _company: str
    _has_masters: bool = False
    _has_doctorate: bool = False


    @property
    def type(self) -> str:
        return self._type


    @property
    def company(self) -> str:
        return self._company


    @property
    def has_masters(self) -> bool:
        return self._has_masters


    @property
    def has_doctorate(self) -> bool:
        return self._has_doctorate


    @type.setter
    def type(self, type: str) -> None:
        self._type = type

      
    @company.setter
    def company(self, company: str) -> None:
        self._company = company  

            
    @has_masters.setter
    def has_masters(self, has_masters: bool) -> None:
        self._has_masters = has_masters  

                    
    @has_doctorate.setter
    def has_doctorate(self, has_doctorate: bool) -> None:
        self._has_doctorate = has_doctorate   


    def talk(self) -> str:
        print(f'Hello! My name is {self._first_name} {self._last_name}, I am a {self._type} engineer that works {self.weekly_hours} a week at {self.company} and I have a salary of {self._salary}.')
        print(f'I have a masters degree: {self.has_masters}')
        print(f'I have a masters degree: {self.has_doctorate}')