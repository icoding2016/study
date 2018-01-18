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
    def show(self):
        print("B::show()")
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
        print("base::__init__ called before Class B2 init..")
        self.inst_var = 2   # initiate the instance's inst_var, not changing the base instance's inst_var 
    def func(self):
        print("B2::func(), then explicitly call base.func()")
        super(B2, self).func()
    def changeSelfClassVar(self):
        self.class_var = 2  # this add a var to the instance and assign 2, not changing the B::class_var
        print("B2: self.class_var -> %s" % self.class_var)
    def changeClassVar(self):
        B.class_var = 22    # this modifies the 'class var' (static)
        print("B2: class_var -> %s" % B.class_var)


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
    print("-"*10)
    b2.changeSelfClassVar()
    b.show()  # self.inst_var still None, 'static' B.class_var not changed.
    b2.changeClassVar()
    b.show()

