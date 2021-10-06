#include <iostream>
#include <vector>
using namespace std;


class NoName
{
    int a, b;
    public:
        NoName(int i, int j) { a=i; b=j; };
        friend ostream& operator << (ostream& o, const NoName & data);
    
};

ostream & operator << (ostream& o, const NoName & data)
{
    o << "NoName{" << "a="  << data.a << ", " << "b=" << data.b << "}";
    return o;
};


class SomeName
{
    int a, b;
    int ca[4];
    int d = 4;  //C++11 only
    public:
        SomeName(): a{1}, b{2}, ca{31,31,33,34} {};  //C++11, member array initializer
        friend ostream& operator << (ostream& o, const SomeName& data);
};

ostream& operator << (ostream& o, const SomeName& data)
{
    o << "SomeName: {a=" << data.a << ", b=" << data.b << ", ca=" << data.ca << ", d=" << data.d << "}";
    return o;
};

int main()
{
    int arr[3] {1,2,3};
    vector<int> vi {11, 12, 13};

    NoName  nn1(1,2);
    NoName  nn2 {1,2};  //C++11 only. Equivalent to: C c(1,2);

    SomeName sn;

    std::cout << "arr: " << arr << endl;
    std::cout << "nn1: " << nn1 << endl;
    std::cout << "nn2: " << nn2 << endl;
    std::cout << "sn: " << sn << endl;
    //std::cout << "vi: " << vi << endl;

}


