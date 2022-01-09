#include <Worker.h>

class Lawyer:public Worker
{
    private:

        string _law_firm;
        static int _lawyer_count;

    public:

        Lawyer(string fname, string lname, string g, string h, int w, int age, int hours, int salary, string law_firm);
        ~Lawyer();
        string law_firm(void);
        void law_firm(string law_firm);

};