import collections


def elemCounter(A):
    D = dict()

    m = 0
    for x in A:
        if x not in D.keys():
            D[x] = 1
        else:
            D[x] += 1
        if m < D[x]:
            m = D[x]

    print("max counter={}".format(m))
    return D
    

def test():
    
    A = [4,3,4,4,4,2]
    # C = elemCounter(A)
    C = collections.Counter(A)
    print(C)
    print(type(C))

def testBasic():
    L = []
    L.append(('a', None))
    L.append((None, 2))
    print(L)
    L[0] = (L[0][0], 1)
    L[1] = ('b', L[1][1])
    print(L)


test()
testBasic()
