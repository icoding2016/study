# Counting sort is used when: there are smaller integers with multiple counts.
# This sorting technique is effective when the difference between different keys are not so big, 
# otherwise, it can increase the space complexity 
# linear complexity is the need 


# T(N+K)   -- 2N+2K  (N:the number of elements, K:the max element)
# S(K)     -- the counter size (the max element)
def counting_sort(data:list[int])->list[int]:
    if not data:
        return data
    counter = [0] * (max(data)+1)   # init counter with max(data)+1
    for i in data:
        counter[i] += 1
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]
    i = len(counter)-1
    while i >= 0:
        while counter[i] > 0: 
            data[counter[i]-1] = i      # must go from right(max) to left
            counter[i] -= 1
        i -= 1
    return data


def test():
    d = [7,5,7,2,0,3,4,4,1,4,6]
    print(counting_sort(d))


test()


