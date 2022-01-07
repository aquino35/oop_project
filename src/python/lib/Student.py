#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dataclasses import dataclass
from .person import Person
from typing import ClassVar


@dataclass
class Student(Person):
    """## Help on the Student module:
    ----------------------------------
    ### Name

        Student 

    ---------------------
    ### Description 

        The student class is developed to simulate a person that is a student. 

        This class inherits attributes and methods from the Person class.

        @param first_name - first name of student. 

        @param last_name - last name of student.

        @param gender - gender of student.

        @param height - height of student. 

        @param weight - weight of student.

        @param age - age of student. 

        @param institution - institution of the student.

        @param major - major of the student.

        @property decorator: getters for class. 

        @setter decorator: setters for class.

        @example: student = Student("Osvaldo", "Aquino", "M", "5'8", 170, 25, "UPRM", "ICOM")

    ---------------------
    ### Package Contents

        - _first_name
        - _last_name
        - _gender
        - _height
        - _age
        - _institution
        - _major
        - _person_count 
        - _student_count
        - talk()
        - calculate()
        - first_name() || first_name(first_name:str)
        - last_name() || last_name(last_name:str)
        - gender() || gender(gender:str)
        - weight() || weight(weight:int)
        - age() || age(age:int)
        - institution() || institution(institution:str)
        - major() || major(major:str)

    ---------------------
    @author: Osvaldo Aquino
    """

    _institution: str # represents institution of the student
    _major : str # represents major of the student
    _student_count : ClassVar[int] = 0 # static variable used to keep track of each student that is created.


    def __post_init__(self):
        """ Post init function used to increment the global class variables used in this object."""

        Student._person_count+=1
        Student._student_count+=1


    @property
    def institution(self) -> str:
        """ @return: Institution of the student.
            @example: student.institution """

        return self._institution


    @property
    def major(self) -> str:
        """ @return: Major of the student.
            @example: student.major """

        return self._major


    @institution.setter
    def institution(self, institution: str) -> None:
        """ Sets the institution attribute of the student given a string.
            @param institution: String that represents the new institution that will be set.
            @example: student.institution = "UPRM" """

        self._institution = institution


    @major.setter
    def major(self, major: str) -> None:
        """ Sets the major attribute of the student given a string.
            @param major: String that represents the new major that will be set.
            @example: student.major = "ICOM" """

        self._major = major


    def talk(self) -> str:
        """ Prints out useful information about the student object.
            @example: student.talk()"""

        print(f'Hello! My name is {self._first_name} {self._last_name}, I am a student at {self.institution}, studying {self._major}')

    
    def calculate(self, *args: int) -> str:
        """ Calculates the final grade of a student given a set of grades.
            @param *args: Integers representing all the grades the student has accumulated.
            @print: The final grade of the student
            @example: student.calculate(100,100,80,100)
            @example: student.calculate(90,85) """

        num_grades = len(args)
        final_grade = sum(args)/num_grades

        print(f'The final grade is: {final_grade}')