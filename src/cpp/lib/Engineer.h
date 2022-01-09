#include <worker.h>

class Engineer:public Worker
{
    private:

        string _type;
        string _company;
        bool _has_masters;
        bool _has_doctorate;
        static int _engineer_count;
    

    public:

        Engineer(string fname, string lname, string g, string h, int w, int age, int hours, int salary, string type, string comp, bool masters, bool doctorate);
        ~Engineer();
        string type();
        string company();
        bool has_masters();
        bool has_doctorate();
        void type(string type);
        void company(string company);
        void has_masters(bool has_masters);
        void has_doctorate(bool has_doctorate);


};