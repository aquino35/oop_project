from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar

@dataclass
class Person(ABC):
    """
    TODO: Document

    @property decorator -> getters for class 
    @setter decorator -> setters for class
    """

    _first_name : str
    _last_name : str
    _gender : str
    _height : str
    _weight : int
    _age : int = 0
    #_person_count : ClassVar[int] += 1


    @property
    def first_name(self) -> str:
        return self._first_name


    @property
    def last_name(self) -> str:
        return self._last_name


    @property
    def gender(self) -> str:
        return self._gender


    @property
    def height(self) -> str:
        return self._height


    @property
    def weight(self) -> int:
        return self._weight


    @property
    def age(self) -> int:
        return self._age


    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self._first_name = first_name

    
    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self._last_name = last_name


    @gender.setter
    def gender(self, gender: str) -> None:
        self._gender = gender

    
    @height.setter
    def height(self, height: str) -> None:
        self._height = height

    
    @weight.setter
    def weight(self, weight: int) -> None:
        self._weight = weight


    @age.setter
    def age(self, age: int) -> None:
        self._age = age


    @abstractmethod
    def talk() -> str:
        pass