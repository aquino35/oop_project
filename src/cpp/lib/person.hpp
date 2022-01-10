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
    
        /* getters */
        virtual std::string first_name() =  0; 
        virtual std::string last_name() =  0; 
        virtual std::string gender() =  0;
        virtual std::string height() =  0; 
        virtual std::string weight() =  0; 

        /* setters */
        virtual void first_name(std::string first_name) =  0; 
        virtual void last_name(std::string last_name) =  0; 
        virtual void gender(std::string gender) =  0; 
        virtual void height(std::string height) =  0; 
        virtual void age(int age) =  0; 

        /* Allows each person to talk. */
        virtual void talk() =  0; 

        //Person(std::string fname, std::string lname, std::string g, std::string h, int w, int age);

        /* Abstract destructor */
        virtual ~Person() = 0;
};

#endif