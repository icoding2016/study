class A(object):
    clsAttr = "class attr in A"
    clsAttr2 = "class attr2 in A"

    @classmethod
    def setupAttr(cls):
        cls.clsAttr3 = "class attr3 initiated in method"

class AA(A):
    clsAttr = "class attr in AA"
    


def test():
    a = A()
    aa = AA()

    print(A.clsAttr)
    print(AA.clsAttr)
    print(AA.clsAttr2)

    print('------instance------')
    print(a.clsAttr)
    print(a.clsAttr2)
    print(aa.clsAttr)
    print(aa.clsAttr2)

    #print(aa.clsAttr3)     # AttributeError: 'AA' object has no attribute 'clsAttr3' 
    A.setupAttr()
    print(aa.clsAttr3)



if __name__ == "__main__":
    test()
