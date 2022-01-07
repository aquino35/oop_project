#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""


from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar
import itertools


@dataclass
class Person(ABC):
    """
    ## Help on Person module:
    ---------------------
    
    ### Name
        Person
        
    ---------------------

    ### Description 
        The person class is an abstact base class used to create the base person of the collection.
        @property decorator: getters for class 
        @setter decorator: setters for class
    ---------------------

    ### Package Contents
        - _first_name
        - _last_name
        - _gender
        - _height
        - _age
        - _person_count 
        - talk()
        - first_name() || first_name(first_name:str)
        - last_name() || last_name(last_name:str)
        - gender() || gender(gender:str)
        - weight() || weight(weight:int)
        - age() || age(age:int)
        - person_count()
    ---------------------

    @author: Osvaldo Aquino
    """

    _first_name : str # represents first name of person
    _last_name : str # represents last name of person 
    _gender : str # represents gender of person 
    _height : str # represents height of person 
    _weight : int # represents weight of person 
    _age : int # represents age of person
    _person_count : ClassVar[int] = 0 # static variable the increments everytime a person is created.


    @abstractmethod
    def talk(self) -> str:
        """ Abstract method to be implemented in the other objects."""
        pass


    @property
    def first_name(self) -> str:
        """ @return: First name of the person. """
        return self._first_name


    @property
    def last_name(self) -> str:
        """ @return: Last name of the person. """
        return self._last_name


    @property
    def gender(self) -> str:
        """ @return: The gender of the person."""
        return self._gender


    @property
    def height(self) -> str:
        """ @return: The height of the person."""
        return self._height


    @property
    def weight(self) -> int:
        """ @return: The weight of the person."""
        return self._weight


    @property
    def age(self) -> int:
        """ @return: The age of the person."""
        return self._age

    
    @property
    def person_count(self) -> int:
        """ @return: The number of people currently created. """
        return Person._person_count
    

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        """ Sets the first name of the person given a string.
            @param first_name: String that represents the new first name that will be set. """
        self._first_name = first_name

    
    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """ Sets the last name of the person given a string.
            @param last_name: String that represents the new last name that will be set. """
        self._last_name = last_name


    @gender.setter
    def gender(self, gender: str) -> None:
        """ Sets the gender of the person given a string.
            @param gender: String that represents the new gender that will be set. """
        self._gender = gender

    
    @height.setter
    def height(self, height: str) -> None:
        """ Sets the height of the person given a string.
            @param height: String that represents the new height that will be set. """
        self._height = height

    
    @weight.setter
    def weight(self, weight: int) -> None:
        """ Sets the weight of the person given an integer.
            @param weight: Integer that represents the new weight that will be set. """
        self._weight = weight


    @age.setter
    def age(self, age: int) -> None:
        """ Sets the age of the person given an integer.
            @param age: Integer that represents the new age that will be set. """
        self._age = age