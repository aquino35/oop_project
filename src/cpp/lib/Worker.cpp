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

#include "lib/headers/worker.hpp"


Worker::Worker(std::string fname, std::string lname, std::string g, std::string h, int w, int age, int hours, int salary)
{
    this->_first_name = fname;
    this-> _last_name = lname;
    this->_gender = g;
    this->_height = h;
    this->_weight = w;
    this->_age = age;
    this->_weekly_hours = hours;
    _person_count++;
    _worker_count++;
}

void Worker::talk(void)
{
    std::cout << "Hello! My name is" << this->_first_name << this->_last_name << ", I am a workers that works"
    << this->_weekly_hours << "a week and I have a salary of" << this->_salary << "." << std::endl;;
}
