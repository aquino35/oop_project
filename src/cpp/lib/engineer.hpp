/**
 * @file engineer.hpp
 * @author Osvaldo Aquino (osvaldo.aquino@upr.edu)
 * @brief TODO: Document - Holds declarations for a person that is an engineer
 * @version 0.1
 * @date 2022-01-10
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <cpp/lib/worker.hpp>

#ifndef __ENGINEER_H_INCLUDED__  
#define __ENGINEER_H_INCLUDED__ 


class Engineer:public Worker
{
    private:

        std::string _type;
        std::string _company;
        bool _has_masters;
        bool _has_doctorate;
        static int _engineer_count;
    

    public:

        Engineer(std::string fname, std::string lname, std::string g, std::string h, int w, int age, int hours, int salary, std::string type, std::string comp, bool masters, bool doctorate);
        ~Engineer();
        std::string type();
        std::string company();
        bool has_masters();
        bool has_doctorate();
        void type(std::string type);
        void company(std::string company);
        void has_masters(bool has_masters);
        void has_doctorate(bool has_doctorate);


};

#endif