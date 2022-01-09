#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dataclasses import dataclass
from .person import Person
from typing import ClassVar


@dataclass
class Worker(Person):
    """Help on the Worker module:
    
    Name

        Worker 

    
    Description 

        The worker class is developed to simulate a person that is a worker. 

        This class inherits attributes and methods from the Person class.

        - property decorator: getters for class. 

        - setter decorator: setters for class.

    Args

        first_name: first name of worker. 

        last_name: last name of worker.

        gender: gender of worker.

        height: height of worker. 

        weight: weight of worker.

        age: age of worker. 

        weekly hours: weekly hours of worker.

        salary: salary of worker.


    Usage

        worker = Worker("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 50000)

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
        - talk()
        - first_name() || first_name(first_name:str)
        - last_name() || last_name(last_name:str)
        - gender() || gender(gender:str)
        - weight() || weight(weight:int)
        - age() || age(age:int)
        - weekly_hours() || weekly_hours(weekly_hours:int)
        - salary() || salary(salary:int)

    Author
        
        Osvaldo Aquino
    """

    _weekly_hours: int # represents weekly hours of the worker
    _salary : int # represents the salary of the worker
    _worker_count : ClassVar[int] = 0 # static variable used to keep track of each worker that is created.


    def __post_init__(self):
        """ Post init function used to increment the global class variables used in this object."""

        Worker._person_count+=1 
        Worker._worker_count+=1


    @property
    def weekly_hours(self) -> int:
        """ Returns

                Weekly hours of the worker.

            Usage

                worker.weekly_hours """

        return self._weekly_hours


    @property
    def salary(self) -> int:
        """ Returns

                Salary of the worker.

            Usage

                worker.salary """

        return self._salary


    @weekly_hours.setter
    def weekly_hours(self, weekly_hours: int) -> None:
        """ Sets the weekly hours attribute of the worker given an integer.

            Args

                weekly_hours(int): Represents the new weekly hours that will be set.

            Usage

                worker.weekly_hours = 40 """

        self._weekly_hours = weekly_hours


    @salary.setter
    def salary(self, salary: int) -> None:
        """ Sets the salary attribute of the worker given an integer.
            
            Args

                salary(int): Represents the new salary that will be set.

            Usage

                worker.salary = 90000 """

        self._salary = salary


    def talk(self) -> str:
        """ Prints out useful information about the worker object.

            Usage
            
                worker.talk()"""

        print(f'Hello! My name is {self._first_name} {self._last_name}, I am a worker that works {self.weekly_hours} a week and I have a salary of {self._salary}.')