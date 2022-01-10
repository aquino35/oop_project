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
#include <cpp/lib/doctor.hpp>


Doctor::Doctor(std::string fname, std::string lname, std::string g, std::string h, int w, int age, int hours, int salary, std::string type)
{
    this->_first_name = fname;
    this-> _last_name = lname;
    this->_gender = g;
    this->_height = h;
    this->_weight = w;
    this->_age = age;
    this->_weekly_hours = hours;
    this->_type = type;
    _person_count++;
    _worker_count++;
    _doctor_count++;
}
