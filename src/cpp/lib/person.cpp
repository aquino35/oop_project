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

#include <cpp/lib/person.hpp>


std::string Person::first_name(void)
{
    return this->_first_name;
}


std::string Person::gender(void)
{
    return this->_gender;
}


std::string Person::height(void)
{
    return this->_height;
}


std::string Person::weight(void)
{
    return this->_weight;
}


int Person::age(void)
{
    return this->_age;
}


void Person::first_name(std::string first_name)
{
    this->_first_name = first_name;
}


void Person::last_name(std::string last_name)
{
    this->_last_name = last_name;
}


void Person::gender(std::string gender)
{
    this->_gender = gender;
}

void Person::height(std::string height)
{
    this->_height = height;
}


void Person::age(int age)
{
    this->_age = age;
}