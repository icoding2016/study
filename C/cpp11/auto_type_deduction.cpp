/*
in older version C++, auto designates an object with automatic storage type.
C++11 has changed 'auto' keyword's meaning; now it declares an object whose type is deducible from its initializer.
*/

#include <iostream>
#include <vector>
using namespace std;




template <class T> const char* getType(const T&);

void test(vector<int> &vi)
{
    auto ai = vi;
    for(auto & i: ai)
        std::cout << "vi=" << i << ", type: " << getType(i) << endl;
}


template <class T>
const char* getType(const T&)
{
    // cout << __PRETTY_FUNCTION__ << "\n";
    return __PRETTY_FUNCTION__;
}



int main()
{
    vector<int> vi{10,20,30};  //vi(3, 10);      
    test(vi);

}