#include <iostream>
#include <vector>


template <class T> void printType(const T&)
{
    std::cout << __PRETTY_FUNCTION__ << "\n";
}

int main()
{
    auto x = 10.0;
    printType(x);
}
