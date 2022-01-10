/**
 * @file doctor.hpp
 * @author Osvaldo Aquino (osvaldo.aquino@upr.edu)
 * @brief TODO: Document - Abstract class for person collection.
 * @version 0.1
 * @date 2022-01-10
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <cpp/lib/worker.hpp>

#ifndef __DOCTOR_H_INCLUDED__  
#define __DOCTOR_H_INCLUDED__ 
class Doctor:public Worker
{
    public:

        Doctor() = default;
        Doctor(std::string fname, std::string lname, std::string g, std::string h, int w, int age, int hours, int salary, std::string type);
        ~Doctor();

        // getters
        std::string type(); 
        
        // setters
        void type(std::string type); 

    private:

        std::string _type;
        static int _doctor_count;
};
#endif