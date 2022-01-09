#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dataclasses import dataclass
from typing import ClassVar
from .worker import Worker


@dataclass
class Doctor(Worker):
    """Help on the Doctor module:

    Name

        Doctor 

    Description 

        The doctor class is developed to simulate a person that is a doctor.

        This class inherits attributes and methods from the Worker class.

        - property decorator: getters for class. 
        - setter decorator: setters for class.

    Args

        first_name: first name of doctor. 

        last_name: last name of doctor.

        gender: gender of doctor.

        height: height of doctor. 

        weight: weight of doctor.

        age: age of doctor. 

        weekly hours: weekly hours of doctor.

        salary: salary of doctor.

        type: type of doctor.

    Usage
        
        doctor = Doctor("Ale", "Pagan", "M", "5'8", 170, 22, 40, 90000, "Generalist")

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
        - _doctor_count
        - talk()
        - first_name() || first_name(first_name:str)
        - last_name() || last_name(last_name:str)
        - gender() || gender(gender:str)
        - weight() || weight(weight:int)
        - age() || age(age:int)
        - weekly_hours() || weekly_hours(weekly_hours:int)
        - salary() || salary(salary:int)
        - type() || type(type:str)

    Author 

        Osvaldo Aquino
    """

    _type: str # represents the type of doctor.
    _doctor_count : ClassVar[int] = 0 # static variable used to keep track of each doctor that is created.


    def __post_init__(self):
        """ Post init function used to increment the global class variables used in this object."""

        Doctor._person_count+=1
        Doctor._worker_count+=1
        Doctor._doctor_count+=1


    @property
    def type(self) -> str:
        """ Returns

                type of doctor.

            Usage

                doctor.type """

        return self._type


    @type.setter
    def type(self, type: str) -> None:
        """ Sets the type attribute of the doctor given a string.

            Args

                type(str): Represents the new type that will be set.

            Usage

                doctor.type = "Cardiologist" """

        self._type = type


    def talk(self) -> str:
        """ Prints out useful information about the doctor object.

            Usage
            
                doctor.talk()"""

        print(f'Hello! My name is {self._first_name} {self._last_name}, I am a {self._type} doctor that works {self.weekly_hours} a week and I have a salary of {self._salary}.')