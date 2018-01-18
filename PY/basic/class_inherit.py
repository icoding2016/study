#!/usr/bin/python

from __future__ import print_function

class B(object):
    class_var = None
    def __init__(self):
        print("Class B init..")
        self.inst_var = 0
    def func(self):
        print("B::func()")
        print("class_var=%s" % self.class_var)
        print("inst_var=%s" % self.inst_var)



class B1(B):
    def __init__(self):
        print("Class B1 init..")
        self.inst_var = 1
    def func(self):
        print("B1::func()")

class B2(B):
    def __init__(self):
        super(B2, self).__init__()
        print("Class B2 init..")
        self.inst_var = 2
    def func(self):
        print("B2::func()")
        super(B2, self).func()

if "__main__" in  __name__:
    print("-"*20)
    b = B()
    b.func()
    print("-"*20)
    b1 = B1()
    b1.func()
    print("-"*20)
    b2 = B2()
    b2.func()

