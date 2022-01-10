#include <iostream>
#include <string.h>
#include "lib/headers/worker.hpp"



using namespace std;

int main()
{
    string hello_world = "Hello World";
    cout << hello_world;

    Worker* Osvaldo = new Worker("Osvaldo", "Aquino", "M", "5'8", 170, 22, 40, 50000);

    Osvaldo->talk();
}