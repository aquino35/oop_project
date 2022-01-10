/**
 * @file student.hpp
 * @author Osvaldo Aquino (osvaldo.aquino@upr.edu)
 * @brief TODO: Document - Abstract class for person collection.
 * @version 0.1
 * @date 2022-01-10
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <lib/headers/person.hpp>


#ifndef __STUDENT_H_INCLUDED__  
#define __STUDENT_H_INCLUDED__ 
class Student:public Person
{
    public:

        Student(std::string fname, std::string lname, std::string g, std::string h, int w, int age, std::string ints, std::string major);
        ~Student();

        virtual void talk();
        void calculate(int* args);

        // getters
        std::string institution(void);
        std::string major(void);

        //setters
        void institution(std::string institution);
        void major(std::string major);

    private:
    
        std::string _institution;
        std::string _major;
        static int _student_count;
};
#endif