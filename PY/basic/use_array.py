import numpy as np
import sys



test_data = [
    [11,12,13],
    [21,22,23],
    [31,32,33],
]

def test():
    arr = np.array(test_data)
    print(arr)
    print(arr.dtype)
    print(arr.size)
    print(arr.ndim)
    print(arr.shape)

    arr_f = np.array(test_data, dtype=float)
    print(arr_f)

    arr_r = np.random.random((3,3))
    print(arr_r)

    arr_full = np.full((3,3), 7, dtype=float)
    print(arr_full)

    arr_slice = arr[:2, ::2]
    print(arr_slice)
    arr_slice = arr[0:2, ::-1]
    print(arr_slice)

    print(arr * 2)
    print(arr + 100)

    print(np.arange(20))

    print(sys.getsizeof(np.arange(1000)))
    print(sys.getsizeof(list(range(1000))))


test()
