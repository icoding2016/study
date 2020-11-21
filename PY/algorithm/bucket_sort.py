# Bucket Sort
# Bucket sort is used when:
# - input is uniformly distributed over a range.
# - there are floating point values

import random


# T()
def bucket_sort(data:list, k:int=None) -> list:
    '''bucket sort
       k: bucket size
    '''
    if not data:
        return data
    if None == k:
        k = int(len(data)/5)
    bucket = [[] for i in range(k)]
    mn = min(data)
    mx = max(data)
    for x in data:
        bucket[int(k*(x-mn-1)/(mx-mn))].append(x)
    #print(bucket)
    data = []
    for b in bucket:
        data.extend(next_sort(b))
    return data


def next_sort(data:list) -> list:
    return sorted(data)   # we can pick a sorting algorithm for next sort, but  simply use python lib here.


def test():
    data = []
    size = 50
    for i in range(size):
        data.append(random.randint(0, size))
    
    print(bucket_sort(data))
    print(bucket_sort(data, k=20))


test()

