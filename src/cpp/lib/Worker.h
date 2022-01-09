#include <person.h>

class Worker:public Person
{
    private:

        int _weekly_hours;
        int _salary;
        static int _worker_count;

    public:

        Worker(string fname, string lname, string g, string h, int w, int age, int hours, int salary);
        ~Worker();
        int weekly_hours();
        int salary();
        void weekly_hours(int weekly_hours);
        void salary(int salary);
};