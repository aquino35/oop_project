#include <person.h>

class Student:public Person
{
    private:
        string _institution;
        string _major;
        static int _student_count;

    public:

        Student(string fname, string lname, string g, string h, int w, int age, string ints, string major);
        ~Student();
        string institution(void);
        string major(void);
        void institution(string institution);
        void major(string major);
        void calculate(int* args);
};