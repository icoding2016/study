import os
import sys

import unittest
import unittest.mock as mock


class EgClass(object):
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
    @mock.patch("sys.modules", return_value="a fake result for sys.modules")
    @mock.patch("sys.version")
    @mock.patch("os.path")
    def testMultiPatch(self, mock1, mock2, mock3):
        mock1.return_value = "fake os.path"
        mock2.return_value = "fake sys.version"
        print("mock1 (os.path): {}".format(os.path()))
        print("mock2 (sys.version): {}".format(sys.version()))
        print("mock3 (sys.modules): {}".format(sys.modules()))

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
    tester = Tester()    
    m = mock.MagicMock()

    # Todo:

def test_mockPatch():
    tester = Tester()    
    tester.testPatchA()
    tester.testPatchB1()
    tester.testMultiPatch()

def test():
    test_mockMethod()
    test_mockPatch()



if __name__ == '__main__':
    test()
