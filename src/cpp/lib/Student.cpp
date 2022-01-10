/**
 * @file person.hpp
 * @author Osvaldo Aquino (osvaldo.aquino@upr.edu)
 * @brief TODO: Document - Abstract class for person collection.
 * @version 0.1
 * @date 2022-01-10
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <cpp/lib/student.hpp>


Student::Student(std::string fname, std::string lname, std::string g, std::string h, int w, int age, std::string ints, std::string major)
{
    this->_first_name = fname;
    this-> _last_name = lname;
    this->_gender = g;
    this->_height = h;
    this->_weight = w;
    this->_age = age;
    this->_institution = ints;
    this->_major = major;
    _person_count++;
    _student_count++;
}