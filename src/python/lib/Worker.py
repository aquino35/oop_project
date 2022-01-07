#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dataclasses import dataclass
from .person import Person
from typing import ClassVar


@dataclass
class Worker(Person):
    """## Help on the Worker module:
    --------------------------------
    ### Name

        Worker 

    ---------------------
    ### Description 

        The worker class is developed to simulate a person that is a worker. 

        This class inherits attributes and methods from the Person class.

        @param first_name - first name of worker. 

        @param last_name - last name of worker.

        @param gender - gender of worker.

        @param height - height of worker. 

        @param weight - weight of worker.

        @param age - age of worker. 

        @param weekly hours - weekly hours of worker.

        @param salary - salary of worker.

        @property decorator: getters for class. 

        @setter decorator: setters for class.

        @example: worker = Worker("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 50000)

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
        - talk()
        - first_name() || first_name(first_name:str)
        - last_name() || last_name(last_name:str)
        - gender() || gender(gender:str)
        - weight() || weight(weight:int)
        - age() || age(age:int)
        - weekly_hours() || weekly_hours(weekly_hours:int)
        - salary() || salary(salary:int)

    ---------------------
    @author: Osvaldo Aquino
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
        """ @return: Weekly hours of the worker.
            @example: worker.weekly_hours """

        return self._weekly_hours


    @property
    def salary(self) -> int:
        """ @return: Salary of the worker.
            @example: worker.salary """

        return self._salary


    @weekly_hours.setter
    def weekly_hours(self, weekly_hours: int) -> None:
        """ Sets the weekly hours attribute of the worker given an integer.
            @param weekly_hours: Integer that represents the new weekly hours that will be set.
            @example: worker.weekly_hours = 40 """

        self._weekly_hours = weekly_hours


    @salary.setter
    def salary(self, salary: int) -> None:
        """ Sets the salary attribute of the worker given an integer.
            @param salary: Integer that represents the new salary that will be set.
            @example: worker.salary = 90000 """

        self._salary = salary


    def talk(self) -> str:
        """ Prints out useful information about the worker object.
            @example: worker.talk()"""

        print(f'Hello! My name is {self._first_name} {self._last_name}, I am a worker that works {self.weekly_hours} a week and I have a salary of {self._salary}.')