/*
C11 feature: Lambda Expression
*/

#include <iostream>
#include <algorithm>

using namespace std;


void test_lambda() 
{
    char s[] = "This is a test string.";
    int upper = 0;
    for_each (s, s+sizeof(s), [&upper](char c) {
        if (isupper(c)) upper++;
    });
    cout << "Count of upper: " << upper << endl;
}


int main()
{
    test_lambda();
}

//main()
