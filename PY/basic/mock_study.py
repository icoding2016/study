# 
# mock.patch vs mock.patch.object:
#   mock.patch() takes a string which will be resolved to an object when applying the patch, mock.patch.object() takes a direct reference.
#   This means that mock.patch() doesn't require that you import the object before patching, 
#   while mock.patch.object() does require that you import before patching.
#   The latter is then easier to use if you already have a reference to the object.
# 
# Scope of mock.Pack
# e.g.
#   a.py
#     -> Defines SomeClass
#   b.py
#     -> from a import SomeClass
#     -> some_function instantiates SomeClass
# Now we want to test some_function but we want to mock out SomeClass using patch(). 
# The problem is that when we import module b, which we will have to do then it imports SomeClass from module a. 
# If we use patch() to mock out a.SomeClass then it will have no effect on our test; module b already has a reference to the real SomeClass and it looks like our patching had no effect.
# The key is to patch out SomeClass where it is used (or where it is looked up). <<====
# In this case some_function will actually look up SomeClass in module b, where we have imported it. 
# The patching should look like:
#   @patch('b.SomeClass')
# 
# #

import os
import sys

import unittest
import unittest.mock as mock


class EgClass(object):
    def __init__(self):
        self.attr1=None
        self.attr2=None

    def A(self):
        print("EgClass::A()")
        return 'A'

    def B(self):
        print("EgClass::B()")
        return 'B'

class Tester(unittest.TestCase):
    def __init__(self):
        self.name = 'Tester'
        self.egClass = EgClass()

    def funcA(self, arg1):
        print("Tester.funcA({})".format(arg1))
        return 'funcA'

    @mock.patch("sys.version", return_value="a fack version info A")
    def testPatchA(self, mockEgA):

        r1 = sys.version()
        print(r1)

        self.assertTrue(mockEgA.called)

    def testPatchB1(self):
        with mock.patch("sys.version", return_value="a fack version info B") as mockEgB:
            r = sys.version()
            print(r)


    # Note: the sequence of mock.patch
    #       the closer the decorator is to the function definition, the earlier it is in the parameter list.
    @mock.patch("sys.modules", return_value="a fake result for sys.modules")
    @mock.patch("sys.version")
    @mock.patch("os.path")
    def testMultiPatch(self, mock1, mock2, mock3):
        mock1.return_value = "fake os.path"
        mock2.return_value = "fake sys.version"
        print("mock1 (os.path): {}".format(os.path()))
        print("mock2 (sys.version): {}".format(sys.version()))
        print("mock3 (sys.modules): {}".format(sys.modules()))

    @mock.patch.object(sys, 'version', return_value='4.2.2')
    @mock.patch('sys.version', return_value='4.1.3')
    def testMockObj(self, mock1, mockobj1):
        print(mock1())
        print(mockobj1())


def test_mockMethod():
    tester = Tester()    

    r = tester.funcA('arg')

    m = mock.MagicMock()
    m.return_value = "mock value"
    tester.funcA = m
    r = tester.funcA()
    print(r)

    tester.funcA(1,2, 'arg3')
    print(tester.funcA.call_count)
    print(tester.funcA.mock_calls)


def test_mockClass():
    m1 = mock.Mock(spec=EgClass, attr1='ATTR1', attr2='ATTR2')
    print(m1.attr1)
    print(m1.attr2)
    #m = mock.MagicMock()
    # Todo:

def test_mockPatch():
    tester = Tester()    
    tester.testPatchA()
    tester.testPatchB1()
    tester.testMultiPatch()
    tester.testMockObj()

def test():
    test_mockMethod()
    test_mockPatch()
    test_mockClass()



if __name__ == '__main__':
    test()
