/*
Implicit Conversion:
In C++, a constructor with only one required parameter is considered an implicit conversion function. 
It converts the parameter type to the class type.

Explicit:
Prefixing the explicit keyword to the constructor prevents the compiler from using that constructor for implicit conversions.

*/

#include <iostream>

using namespace std;


class A
{
    string s;
    public:
        A(string ss): s{ss} { }; 
        A(int n): s{string(n, '_')} { };
        friend ostream& operator << (ostream& o, const A& a);
};

ostream& operator << (ostream& o, const A& a)
{
    o << a.s;
    return o;
};


class B
{
    string s;
    public:
        B(string ss): s{ss} { }; 
        explicit B(int n): s{string(n, '_')} { };
        friend ostream& operator << (ostream& o, const B& a);
};

ostream& operator << (ostream& o, const B& b)
{
    o << b.s;
    return o;
};


void fa(A a)
{
    cout << "fa: " << a << endl;
};


void fb(B b)
{
    cout << "fb: " << b << endl;
};



int main()
{
    A a = 'x';  // The character 'x' is implicitly converted to int and then A(int) 
    cout << a << endl;

    // B b = 'x';  // error: conversion from 'char' to non-scalar type 'B' requested
    // cout << b << endl;
    B b1 = string{"xxx"};
    cout << b1 << endl;
    B b2 = B(10);
    cout << b2 << endl;

    fa(2);                  // OK, implicit conversion
    fa(A(2));               // OK, direct initialization: explicit conversion
    fa(static_cast<A>(2));  // OK, explicit conversion

    //fb(2);                  // error: could not convert '2' from 'int' to 'B' (implicit conversion)
    fb(B(2));               // OK, direct initialization: explicit conversion
    fb(static_cast<B>(2));  // OK, explicit conversion

}