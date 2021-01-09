# Implement a stack with the functions pop, push, inc, isEmpty, and peek. 
# The inc function increases the first n elements of the stack by a value i.  
#
# suppose the data in the stack is int (based on the description of inc func)


class EmptyStackException(Exception):
    pass

class InvalidArgException(Exception):
    pass

class MyStack(object):
    def __init__(self):
        self.data = []
        # self.top = -1
        # self.bottom = -1

    def validateData(self, d):
        if isinstance(d, int):
            return True
        return False

    def push(self, val):
        if self.validateData(val):
            self.data.append(val)
        else:
            raise InvalidArgException("Invalid data type, expecting int")

    def pop(self):
        if self.data:
            return self.data.pop()
        raise EmptyStackException("Empty Stack")

    def peek(self):
        if self.data:
            return self.data[-1]
        raise EmptyStackException("Empty Stack")

    def isEmpty(self):
        return len(self.data) == 0

    def inc(self, n:int, v:int)->None:
        if len(self.data) < n:
            raise InvalidArgException("{} exceed stack size".format(n))
        else:
            for i in range(n):
                self.data[i] += v

    def show(self):
        print(self.data)

    def __len__(self):
        return len(self.data)

def test_fixture(solution):
    testdata = [  # (input, expect),
        # N,ks,ke,b,
        ((), ),
    ]

    for i in range(len(testdata)):
        ret = solution.minKightMoves(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format(testdata[i][0], ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))



def test():
    # s = Solution()
    # test_fixture(s)
    ms = MyStack()
    print("isEmpty: ", ms.isEmpty())
    for i in range(10,101,10):
        ms.push(i)
    ms.show()
    print(ms.peek())
    ms.inc(5, 1)
    ms.show()
    print("isEmpty: ", ms.isEmpty())
    
    ms.pop()
    ms.pop()
    ms.show()
    
    try:
        ms.push("a string")
    except InvalidArgException:
        print("InvalidArgException varified.")

    try:
        for i in range(len(ms)+1):
            print("pop: ",ms.pop())
    except EmptyStackException:
        print("EmptyStackException varified.")
    


test()    
