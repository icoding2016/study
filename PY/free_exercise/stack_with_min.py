# implement a Stack with a minimum() which return the min number in the stack. 
# (A stack that remember current minimum number)
# assume the elements in the stack are int


class EmptyStackException(Exception):
    pass



class StackMin(object):
    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val:int)->None:
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(val if val < self.min[-1] else self.min[-1])
            self.data.append(val)        
    
    def pop(self)->int:
        if not self.data:
            raise EmptyStackException("Stack is empty")
        self.min.pop()
        return self.data.pop()

    def minimum(self):
        if self.min:
            return self.min[-1]
        return None

    def __len__(self)->int:
        return len(self.data)

    def show(self):
        print("data[]: ", self.data)
        print("min[]: ", self.min)



def test_fixture(solution):
    testdata = [  # (input, expect),
        # N,ks,ke,b,
        ((10,(1,2),(5,3),(2,5), ), 3),
        ((10,(1,2),(5,3),(4,5), ), 3),
        ((10,(1,2),(5,3),(4,2), ), -1),     # K2 is in the catchment of bishop
        ((10,(1,2),(4,3),(4,2), ), 4),
        ((10,(1,2),(4,3),(7,2), ), 2),
    ]

    for i in range(len(testdata)):
        ret = solution.minKightMoves(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format(testdata[i][0], ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))



def test():
    s = StackMin()
    #test_fixture(s)
    d = [5,3,8,1,0,9,2,3,7,4,7,8,6]
    for x in d:
        s.push(x)
        s.show()
        print("min: ", s.minimum())
    while len(s):
        print("pop: ", s.pop())
        s.show()
        print("min: ", s.minimum())


test()    



