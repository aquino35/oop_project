/**
 * @file lawyer.hpp
 * @author Osvaldo Aquino (osvaldo.aquino@upr.edu)
 * @brief TODO: Document - Abstract class for person collection.
 * @version 0.1
 * @date 2022-01-10
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <lib/headers/worker.hpp>


#ifndef __LAWYER_H_INCLUDED__  
#define __LAWYER_H_INCLUDED__ 
class Lawyer:public Worker
{
    public:

        Lawyer(std::string fname, std::string lname, std::string g, std::string h, int w, int age, int hours, int salary, std::string law_firm);
        ~Lawyer();

        virtual void talk();

        std::string law_firm(void);
        
        void law_firm(std::string law_firm);

    private:

        std::string _law_firm;
        static int _lawyer_count;
};
#endif