#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dataclasses import dataclass
from typing import ClassVar
from .worker import Worker


@dataclass
class Engineer(Worker):
    """Help on the Engineer module:

    Name

        Engineer 

    Description 

        The engineer class is developed to simulate a person that is an engineer. 

        This class inherits attributes and methods from the Worker class.

        - property decorator: getters for class. 

        - setter decorator: setters for class.

    Args

        first_name: first name of engineer. 

        last_name: last name of engineer.

        gender: gender of engineer.

        height: height of engineer. 

        weight: weight of engineer.

        age: age of engineer. 

        weekly hours: weekly hours of engineer.

        salary: salary of engineer.

        type: type of engineer.

        company: company of engineer.

        has_masters: True is enginner has a masters degree. Default is false.

        has_doctorate: True is enginner has a doctorate degree. Default is false.


    Usage

        engineer = Engineer("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 100000, "Computer", "Home", True)

    Package Contents

        - _first_name
        - _last_name
        - _gender
        - _height
        - _age
        - _weekly_hours
        - _salary
        - _person_count 
        - _worker_count
        - _engineer_count
        - talk()
        - first_name() || first_name(first_name:str)
        - last_name() || last_name(last_name:str)
        - gender() || gender(gender:str)
        - weight() || weight(weight:int)
        - age() || age(age:int)
        - weekly_hours() || weekly_hours(weekly_hours:int)
        - salary() || salary(salary:int)
        - type() || type(type:str)
        - company() || company(company:str)
        - has_masters() || has_masters(has_master:bool)
        - has_doctorate() || has_doctorate(has_master:bool)

    Author 

        Osvaldo Aquino
    """

    _type: str # represents the type of engineer.
    _company: str # represents the company where the engineer works.
    _has_masters: bool = False # represents if the engineers has a masters degree of not.
    _has_doctorate: bool = False # represents if the engineers has a doctorate degree of not.
    _engineer_count : ClassVar[int] = 0 # static variable used to keep track of each engineer that is created.


    def __post_init__(self):
        """ Post init function used to increment the global class variables used in this object."""

        Engineer._person_count+=1
        Engineer._worker_count+=1
        Engineer._engineer_count+=1


    @property
    def type(self) -> str:
        """ Returns

                type of engineer.

            Usage

                engineer.type """

        return self._type


    @property
    def company(self) -> str:
        """ Returns

                company of engineer.

            Usage

                engineer.company """

        return self._company


    @property
    def has_masters(self) -> bool:
        """ Returns

                True if the engineer has a masters degree. Otherwise, False.

            Usage

                engineer.has_masters """

        return self._has_masters


    @property
    def has_doctorate(self) -> bool:
        """ Returns

                True if the engineer has a doctorate degree. Otherwise, False.

            Usage

                engineer.has_doctorate """

        return self._has_doctorate


    @type.setter
    def type(self, type: str) -> None:
        """ Sets the type attribute of the engineer given a string.

            Args

                type(str): Represents the new type that will be set.

            Usage

                engineer.type = "Electrical" """

        self._type = type

      
    @company.setter
    def company(self, company: str) -> None:
        """ Sets the company attribute of the engineer given a string.

            Args

                company(str): Represents the new company that will be set.

            Usage

                engineer.company = "Texas Instrument" """

        self._company = company  

            
    @has_masters.setter
    def has_masters(self, has_masters: bool) -> None:
        """ Sets the has_masters attribute of the engineer given a boolean.

            Args

                has_masters(bool): Represents the new has_masters that will be set.

            Usage

                engineer.has_masters = True """
            
        self._has_masters = has_masters  

                    
    @has_doctorate.setter
    def has_doctorate(self, has_doctorate: bool) -> None:
        """ Sets the has_doctorate attribute of the engineer given a boolean.

            Args

                has_boolean(bool): Represents the new has_doctorate that will be set.

            Usage

                engineer.has_doctorate = True """

        self._has_doctorate = has_doctorate   


    def talk(self) -> str:
        """ Prints out useful information about the engineer object.

            Usage

                engineer.talk() """

        print(f'Hello! My name is {self._first_name} {self._last_name}, I am a {self._type} engineer that works {self.weekly_hours} a week at {self.company} and I have a salary of {self._salary}.')
        print(f'I have a masters degree: {self.has_masters}')
        print(f'I have a doctorate degree: {self.has_doctorate}')