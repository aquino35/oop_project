/**
 * @file worker.hpp
 * @author Osvaldo Aquino (osvaldo.aquino@upr.edu)
 * @brief TODO: Document - Abstract class for person collection.
 * @version 0.1
 * @date 2022-01-10
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <cpp/lib/person.hpp>


#ifndef __WORKER_H_INCLUDED__  
#define __WORKER_H_INCLUDED__ 

class Worker:public Person
{
    private:

        int _weekly_hours;
        int _salary;
        static int _worker_count;

    public:

        Worker(std::string fname, std::string lname, std::string g, std::string h, int w, int age, int hours, int salary);
        ~Worker();
        int weekly_hours();
        int salary();
        void weekly_hours(int weekly_hours);
        void salary(int salary);
};

#endif