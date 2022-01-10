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

#include <string>                                                              
#ifndef __PERSON_H_INCLUDED__  
#define __PERSON_H_INCLUDED__ 


class Person
{

    private:

        std::string _first_name;
        std::string _last_name;
        std::string _gender;
        std::string _height; 
        std::string _weight;
        int _age;
        static int _person_count;

    public:
    
        // getters
        std::string first_name(); 
        std::string last_name(); 
        std::string gender();
        std::string height(); 
        std::string weight(); 
        int age(); 

        // setters
        void first_name(std::string first_name); 
        void last_name(std::string last_name); 
        void gender(std::string gender); 
        void height(std::string height); 
        void age(int age); 

        // allows each person to talk
        virtual void talk() =  0; 

        //Person(std::string fname, std::string lname, std::string g, std::string h, int w, int age);
};

#endif