import numpy as np
import os

def test_np():
    COL, ROW = 7, 8
    a1 = np.array([[r*10+c for c in range(COL)] for r in range(ROW)])
    print(a1)
    print(a1.size, a1.dtype)
    print(a1[1,2])
    a2 = a1[1:3, 1:3]
    print(a2)
    a3 = a1[1:-1, 1:-1]
    print(a3)
    print(a1[1:-1:2, 1:-1:2])
    c2 = a1[:, 1]
    print(c2)

    X, Y, Z = 4,5,6
    a3d = np.array([[[z*100+y*10+x for x in range(X)] for y in range(Y)] for z in range(Z)])
    print(a3d)
    print(a3d[1:4, 1:3, 2:3])

    z3d = np.zeros((2,3,2))
    print(z3d)

    v2 = np.full((2,2), 33)
    print(v2)

    print(np.full_like(v2, 44))

    r23 = np.random.rand(2,3)
    print(r23)

    ri = np.random.randint(-10,10, (3,2))
    print(ri)

    identity_mtrx = np.identity(5)
    print(identity_mtrx)

    a = np.array([[1,2,3]])
    print(np.repeat(a, 3, axis=0))

    ns = [np.full((n,n), n) for n in range(0, 10)]
    
    ##
    for i in range(1,5):
        ns[-1][i:-i, i:-i] = ns[9-i*2]
    print(ns[9])

    print(a1 * 2)
    print(a1 / 2)

    a = np.array([[1,2,3],[4,5,6]]) 
    b = np.ones((2,3))
    print(a+b)
    print(a * (b * 2))

    print(np.sin(a))
    print(np.cos(a))

    a = np.ones((2,3))
    b = np.full((3,2), 2)
    print(np.matmul(a, b))

    print(a.reshape((3,2)))
    fp = os.path.join(os.path.curdir, 'data.txt')
    np.savetxt(fp, ns[9])

    file_data = np.genfromtxt(fp)
    print(file_data)

    # Boolean masking and davanced indexing
    print(file_data > 5)
    print(file_data[file_data < 4])

    # load data


def test():
    test_np()



test()
