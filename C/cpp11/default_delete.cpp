/*
defaulted function: 
  “=default” instructs the compiler to generate the default implementation for the function.

Deleted functions:
  " =delete"  are useful for preventing object to automatically declares a copy constructor and an assignment operator 
*/


struct NoCopy
{
    int a;
    NoCopy(): a(1) {};
    NoCopy& operator = (const NoCopy&) = delete;
    NoCopy (const NoCopy &) = delete;
};


int main()
{
    NoCopy nc1;
    NoCopy nc2 = nc1;  // error: use of deleted function 'NoCopy::NoCopy(const NoCopy&)'
    NoCopy nc3(nc1);   // error: use of deleted function 'NoCopy::NoCopy(const NoCopy&)'

}

