/*
In C++11 a constructor may call another constructor of the same class:
*/

#include <iostream>
using namespace std;


class C
{
    int x, y;
    public:
        C(int a): x{a}, y{1} {};
        C(): C(2) { cout << x+y << endl; };

};


int main()
{
    C c;

}