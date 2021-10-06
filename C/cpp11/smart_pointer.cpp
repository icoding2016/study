/*
Smart-pointer is a C++11 solution for ‘Garbage Collection’ scenario. 
A Smart Pointer is a wrapper class over a pointer with an operator like * and -> overloaded. 
The objects of the smart pointer class look like normal pointers. 
But, unlike Normal Pointers it can deallocate and free destroyed object memory.

unique_ptr:
  stores one pointer only. We can assign a different object by removing the current object from the pointer.
shared_ptr:
  more than one pointer can point to this one object at a time and it’ll maintain a Reference Counter using use_count() method. 
weak_ptr:
  It’s much more similar to shared_ptr except it’ll not maintain a Reference Counter. 
  In this case, a pointer will not have a stronghold on the object. 
  The reason is if suppose pointers are holding the object and requesting for other objects then they may form a Deadlock.


The best design is to avoid shared ownership of pointers whenever you can. 
However, if you must have shared ownership of shared_ptr instances, avoid cyclic references between them. 

std::weak_ptr is a very good way to solve the dangling pointer problem. 
By just using raw pointers it is impossible to know if the referenced data has been deallocated or not. 
Instead, by letting a std::shared_ptr manage the data, and supplying std::weak_ptr to users of the data, the users can check validity of the data by calling expired() or lock().
std::weak_ptr does not keep its referenced object alive, direct data access through a std::weak_ptr is not possible. 
Instead it provides a lock() member function that attempts to retrieve a std::shared_ptr to the referenced object.

*/

#include <iostream>
#include <memory>
#include <vector>
using namespace std;




/////////////////////////////////////////////////////////////////////
// a psudo smart pointer
template <class T>
class SmartPointer
{
    T * ptr = nullptr;
    public:
        explicit SmartPointer(T* p=nullptr) {  ptr = p;  };
        ~SmartPointer() {  cout << "auto delete ptr:" << ptr << endl;  delete ptr;  };

        T& operator * () {  return *ptr;  };
        T* operator -> () {  return ptr;  };
};

class Square
{
    int a;
    string desc {"Square description."};

    public:
        Square(int x, string y): a{x}, desc{y} { };
        int getA()  {  return a;  };
        int area()  {  return a*a;  };
        string& getDesc()  {  return desc;  };
};


////////////////////////////////////////////////////////////
// std::shared_ptr, std::weak_ptr, 
void test_s_w_ptr()
{
    shared_ptr<Square> sp1(new Square(1, "a 1x1 square"));    // initialize sytle 1
    shared_ptr<Square> sp2{new Square(2, "a 2x2 square")};   // initialize sytle 2
    shared_ptr<Square> sp3, sp;
    sp3.reset(new Square(3, "a 3x3 square"));                // initialize sytle 3 (takes ownership)
    
    cout << "sp1:" << sp1->getDesc() << ", " << sp1 << endl;
    cout << "sp2:" << sp2->getDesc() << ", " << sp2 << endl;
    cout << "sp3:" << sp3->getDesc() << ", " << sp3 << endl;

    weak_ptr<Square> wp1, wp2;
    wp1 = sp1;    
    // std::weak_ptr does not keep its referenced object alive, direct data access through a std::weak_ptr is not possible.
    // Instead it provides a lock() member function that attempts to retrieve a std::shared_ptr to the referenced object.
    // cout << "wp1:" << wp1->getDesc() << endl;  // error: base operand of '->' has non-pointer type 'std::weak_ptr<Square>'
    auto tmp = wp1.lock();
    cout << "wp1:" << tmp->getDesc() << endl;

    {
        shared_ptr<Square> sp4(new Square(4, "a 4x4 square"));
        wp1 = sp4;
        auto tmp = wp1.lock(); cout << "wp1:" << tmp->getDesc() << endl;
        cout << "wp1.expired : " << wp1.expired() << ", wp1.lock: (" << wp1.lock() << ")" << endl;
    }
    cout << "wp1.expired : " << wp1.expired() << ", wp1.lock: (" << wp1.lock() << ")" << endl;

    sp1.reset(new Square(5, "a 5x5 square"));    // deletes old object, acquires new pointer
    wp1 = sp1;
    tmp = wp1.lock(); cout << "wp1:" << tmp->getDesc() << endl;
    cout << "wp1.expired : " << wp1.expired() << ", wp1.lock: (" << wp1.lock() << ")" << endl;

    sp1.reset(new Square(6, "a 6x6 square"));
    wp2 = sp1;
    tmp = wp2.lock(); cout << "wp2:" << tmp->getDesc() << endl;
    if (not wp1.expired())  { tmp = wp1.lock(); cout << "wp1:" << tmp->getDesc() << endl; }
    else  { cout << "w1: expired." << endl; };
};


////////////////////////////////////////////////////////////
// std::unique_ptr,
void test_unique_ptr()
{
    unique_ptr<Square> up{new Square(1, "a 1x1 square")};
    cout << "up:" << up->getDesc() << endl;

    unique_ptr<Square> up1;
    up1 = move(up);
    cout << "up1:" << up1->getDesc() << endl;
    if (up.get())  {  cout << "up:" << up->getDesc() << endl;  };   // up already invalid here

    vector<unique_ptr<Square>> upl;
    for (int i=0; i<5; i++)
    {
        upl.push_back(unique_ptr<Square> (new Square(i, "Square "+ to_string(i))));
    };
    for (const unique_ptr<Square>& u: upl)
    {
        cout << u->getDesc() << endl;
    }

    auto mup = make_unique<Square>(10, "make square 10");
    cout << mup->getDesc() << endl; 
};



int main()
{
    //
    cout << "========= test psudo smart pointer ==========" << endl;
    SmartPointer<string> ptr{new string("test string.")};
    cout << *ptr << endl;

    SmartPointer<Square> pSquare(new Square(10, "a Square str"));
    cout << "Square.a: " << pSquare->getA() << " , Square.desc:" << pSquare->getDesc() << endl;

    cout << "========= test shared / weak pointer ==========" << endl;
    test_s_w_ptr();

    cout << "========= test unique pointer ==========" << endl;
    test_unique_ptr();

}



