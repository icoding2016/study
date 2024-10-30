"""
binary search and insert for sorted array

regarding insert in sorted array, binary search doesn't benefit much for the performance
  since the shift operation is inavitable O(N), 


"""
# 

# Sorted array
#  - binary search
def bsearch(data:list[int], v:int, low:int=None, high:int=None) -> int:
    if None == low:
        low  = 0
    if None == high:
        high = len(data) - 1
    while low <= high:
        m = (low + high) // 2
        if data[m] == v:  return m
        if v < data[m]:   high = m - 1
        else:             low = m + 1
    return -1


# sorted insert_inplace
def sorted_insert_inplace(data:list[int], v:int) -> list[int]:
    if not data:
        return [v]
    if v > data[-1]:
        data.append(v)
        return data
    data.append(v)
    for i in range(len(data)-2,-1,-1):
        if data[i] > v:
            data[i+1] = data[i]
            if i == 0:
                data[0] = v
        else:
            data[i+1] = v
            break
    return data

# sorted_insert_inplace, using bsearch to find location first
# but this doesn't benefit
def sorted_insert_inplace2(data:list[int], v:int) -> list[int]:
    idx = 0
    low, high = 0, len(data) - 1
    if not data:
        return [v,]
    if data[0] > v:
        idx = 0
    elif data[-1] < v:
        idx =  len(data)
    else:
        while low <= high:
            m = (low + high) // 2
            if v == data[m] or data[m] < v:
                low = m + 1
                idx = low
                # if idx >= len(data) or (idx < len(data)-1 and data[idx]>v):
                #     break
            else:
                idx = m
                high = m - 1
                # if idx == 0 or (data[idx-1] <= v):
                #     break
    data.append(None)
    i = len(data) - 1
    while i > idx:
        data[i] = data[i-1]
        i -= 1
    data[idx] = v
    return data

def sorted_insert_joinslice(data:list[int], v:int) -> list[int]:
    if not data:
        return [v, ]
    if v < data[0]:
        return [v] +  data
    elif v >= data[-1]:
        return data + [v]
    idx = 0
    low, high  = 0, len(data) - 1
    while low <= high:
        m = (low + high) // 2
        if data[m] <= v:
            low = m + 1
            idx = low
        else:
            high = m - 1
            idx = m
    return data[:idx] + [v] + data[idx:]

def test_bsearch():
    data = [i for i in range(20)]
    print(bsearch(data, 3))
    print(bsearch(data, 4))
    print(bsearch(data, 20))
    print(bsearch(data, -1))

def test_insert():
    data = [
        [],
        [1],
        [20],
        [i for i in range(20)],
        [1,1,2,3,4,4,5,6,7,7,7,8],
        [7,7,7,7,7,7],
        [1,3,6,8,8,10,20],
    ]
    print("test sorted_insert_inplace")
    for d in data:
        print(sorted_insert_inplace(d, 7))
    print("test sorted_insert_joinslice")
    for d in data:
        print(d, ' -> ', sorted_insert_joinslice(d, 7))

def test():
    # test_bsearch()
    test_insert()

test()