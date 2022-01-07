#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dataclasses import dataclass
from typing import ClassVar
from .worker import Worker


@dataclass
class Lawyer(Worker):
    """## Help on the Lawyer module:
    ---------------------------------
    ### Name

        Lawyer 

    ---------------------
    ### Description 

        The Lawyer class is developed to simulate a person that is a Lawyer. 

        This class inherits attributes and methods from the Worker class.

        @param first_name - first name of lawyer. 

        @param last_name - last name of lawyer.

        @param gender - gender of lawyer.

        @param height - height of lawyer. 

        @param weight - weight of lawyer.

        @param age - age of lawyer. 

        @param weekly hours - weekly hours of lawyer.

        @param salary - salary of lawyer.

        @param law firm - lawfirm of lawyer.

        @property decorator: getters for class. 

        @setter decorator: setters for class.

        @example: lawyer = Lawyer("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 100000, "Vivoni Law Office, LLC")

    ---------------------
    ### Package Contents

        - _first_name
        - _last_name
        - _gender
        - _height
        - _age
        - _weekly_hours
        - _salary
        - _person_count 
        - _worker_count
        - _lawyer_count
        - talk()
        - first_name() || first_name(first_name:str)
        - last_name() || last_name(last_name:str)
        - gender() || gender(gender:str)
        - weight() || weight(weight:int)
        - age() || age(age:int)
        - weekly_hours() || weekly_hours(weekly_hours:int)
        - salary() || salary(salary:int)
        - law_firm() || law_firm(law_firm:str)

    ---------------------
    @author: Osvaldo Aquino
    """

    _law_firm: str # represents the law firm of the worker
    _lawyer_count : ClassVar[int] = 0 # static variable used to keep track of each lawyer that is created.


    def __post_init__(self):
        """ Post init function used to increment the global class variables used in this object."""

        Lawyer._person_count+=1
        Lawyer._worker_count+=1
        Lawyer._lawyer_count+=1
        

    @property
    def law_firm(self) -> str:
        """ @return: Law firm of the lawyer.
            @example: lawyer.law_firm """

        return self._law_firm


    @law_firm.setter
    def law_firm(self, law_firm: str) -> None:
        """ Sets the law firm attribute of the lawyer given a string.
            @param law_firm: String that represents the new law firm that will be set.
            @example: lawyer.law_firm = "Vivoni Law Office, LLC" """

        self._law_firm = law_firm


    def talk(self) -> str:
        """ Prints out useful information about the lawyer object.
            @example: lawyer.talk()"""

        print(f'Hello! My name is {self._first_name} {self._last_name}, I am a lawyer that works {self.weekly_hours} a week at {self._law_firm} and I have a salary of {self._salary}.')