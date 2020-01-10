'''
[Instance Methods]
The first method on MyClass, called method, is a regular instance method. That’s the basic, no-frills method type you’ll use most of the time. 
The method takes at least one parameter, self, which points to an instance of MyClass when the method is called (but of course instance methods can accept more than just one parameter).
Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state.
Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute. This means instance methods can also modify class state.

[Class Methods]
Let’s compare that to the second method, MyClass.classmethod. I marked this method with a @classmethod decorator to flag it as a class method.
Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.
Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. 
However, class methods can still modify class state that applies across all instances of the class.

[Static Methods]
The third method, MyClass.staticmethod was marked with a @staticmethod decorator to flag it as a static method.
This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).
Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.

'''

class A(object):
    data = "A's inital value"

    def __init__(self, value=None):
        if value:
            data = value

    def method(self):
        return "instance method called", self

    def method2(self):
        print(self.data)

    @classmethod
    def classmethod(cls):
        print(cls.data)
        return "class method called", cls

    @staticmethod
    def staticmethod():
        return "static method called"



class AA(A):
    data = "AA's inital value"
    data2 = "AA's special data"

    def __init__(self, value=None, value2=None):
        if value:
            data = value
        if value2:
            self.data2 = value2



def test():
    a = A()
    aa = AA("new value")

    print(a.method)
    print(a.classmethod)
    print(A.classmethod)
    print(A.staticmethod)

    print(AA.classmethod)
    print(A.classmethod)
    print(a.classmethod)

    


if __name__ == "__main__":
    test()