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

#include <lib/headers/student.hpp>


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


void Student::talk(void)
{
    std::cout << "Hello! My name is" << this->_first_name << this->_last_name << 
    ", I am a student at" << this->_institution << "studying" << this->_major"." << std::endl;;
}
