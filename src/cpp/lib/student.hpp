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

#include <cpp/lib/person.hpp>


#ifndef __STUDENT_H_INCLUDED__  
#define __STUDENT_H_INCLUDED__ 

class Student:public Person
{
    private:
        std::string _institution;
        std::string _major;
        static int _student_count;

    public:

        Student(std::string fname, std::string lname, std::string g, std::string h, int w, int age, std::string ints, std::string major);
        ~Student();
        std::string institution(void);
        std::string major(void);
        void institution(std::string institution);
        void major(std::string major);
        void calculate(int* args);
};

#endif