/*
  6 ways to initialize a vector
*/

#include <iostream>
#include <vector>
using namespace std;


template <class T>
void printVector(int n, const vector<T> &v)
{
    std::cout << n << ": ";
    for(auto &i: v)
    {
        std::cout << i << ", ";
    }
    std::cout << endl;

}


int main()
{
    vector<int> v0(3, 10);
    printVector(0, v0);

    vector<int> v1;
    v1.push_back(11);
    v1.push_back(12);
    v1.push_back(13);
    printVector(1, v1);

    vector<int> v2{21,22,23};
    printVector(2, v2);

    int a[] = {31, 32, 33};
    vector<int> v3(a, a+sizeof(a)/sizeof(a[0]));
    printVector(3, v3);

    vector<int> v {41, 42, 43};
    vector<int> v4(v.begin(), v.end());
    printVector(4, v4);

    vector<int> v5(3);
    int value = 50;
    fill(v5.begin(), v5.end(), value);
    printVector(5, v5);

}