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

#include <lib/headers/worker.hpp>


#ifndef __ENGINEER_H_INCLUDED__  
#define __ENGINEER_H_INCLUDED__ 
class Engineer:public Worker
{

    public:

        Engineer(std::string fname, std::string lname, std::string g, std::string h, int w, int age, int hours, int salary, std::string type, std::string comp, bool masters, bool doctorate);
        ~Engineer();

        virtual void talk();

        // getters
        std::string type();
        std::string company();
        bool has_masters();
        bool has_doctorate();
        
        // setters
        void type(std::string type);
        void company(std::string company);
        void has_masters(bool has_masters);
        void has_doctorate(bool has_doctorate);

    private:

        std::string _type;
        std::string _company;
        bool _has_masters;
        bool _has_doctorate;
        static int _engineer_count;
};
#endif