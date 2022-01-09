#pragma once
#include <string>

using namespace std;


/**
* @file person.h
*
* @brief Abstract class for person collection.
*
* @author Osvaldo Aquino
*/

class Person
{

    private:

        string _first_name;
        string _last_name;
        string _gender;
        string _height; 
        string _weight;
        int _age;
        static int _person_count;

    public:
    
        /* getters */
        virtual string first_name() =  0; 
        virtual string last_name() =  0; 
        virtual string gender() =  0;
        virtual string height() =  0; 
        virtual string weight() =  0; 

        /* setters */
        virtual void first_name(string first_name) =  0; 
        virtual void last_name(string last_name) =  0; 
        virtual void gender(string gender) =  0; 
        virtual void height(string height) =  0; 
        virtual void age(int age) =  0; 

        /* Allows each person to talk. */
        virtual void talk() =  0; 

        //Person(string fname, string lname, string g, string h, int w, int age);

        /* Abstract destructor */
        virtual ~Person() = 0;
};