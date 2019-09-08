# class method vs self
'''
Class method:  
    @classmethod       'cls'
    accessible by class, also accessible by instance of the class

Instance method:
    'self'
    only accessible by instance object

'''

class TestClass():

    @classmethod
    def classInit(cls):
        cls.Name = "className"
        cls.Counter = 0    

    @classmethod
    def classCounting(cls):
        cls.Counter += 1

    @classmethod
    def classFunction(cls):
        print("clsName: {}".format(cls.Name))
        print("clsCounter: {}".format(cls.Counter))

    def __init__(cls):
        cls.classInit()



class TestClassObj(TestClass):

    def __init__(self):
        self.Name = "ObjectName"

    def Function(self):
        print("TestObject.Name: {}".format(self.Name))

    # Try visit class method from object
    def AccessClassFunc(self):
        self.classFunction()



if __name__ == "__main__":
    print("--TestClass--")
    C = TestClass()
    C.classFunction()
    C.classCounting()
    C.classFunction()

    # directly call classmethod
    TestClass.classCounting()
    TestClass.classFunction()

    print("--TestClassObj--")
    O = TestClassObj()
    O.Function()
    # indirect call classmethod from instance func
    O.AccessClassFunc()
    # call classmethod by instance
    O.classCounting()
    O.classFunction()
