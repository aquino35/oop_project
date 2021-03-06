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

#include <lib/headers/engineer.hpp>


Engineer::Engineer(std::string fname, std::string lname, std::string g, std::string h, int w, int age, int hours, int salary, std::string type, std::string comp, bool masters, bool doctorate)
{
    this->_first_name = fname;
    this-> _last_name = lname;
    this->_gender = g;
    this->_height = h;
    this->_weight = w;
    this->_age = age;
    this->_weekly_hours = hours;
    this->_type = type;
    this->_company = comp;
    this->_has_masters = masters;
    this->_has_doctorate = doctorate;
    _person_count++;
    _worker_count++;
    _engineer_count++;
}


void Engineer::talk(void)
{
    std::cout << "Hello! My name is" << this->_first_name << this->_last_name << ", I am a" << this->_type << "engineer that works" 
    << this->_weekly_hours << "a week at" << this->_company << "and I have a salary of" << this->_salary << "." << std::endl;;

    std::cout << "I have a masters degree:" << this->_has_masters << std::endl;;

    std::cout << "I have a doctorate degree:" << this->_has_doctorate << std::endl;;
}