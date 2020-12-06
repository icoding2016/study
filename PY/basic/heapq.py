import heapq

def test():
    data = [(30, 'a'), (25, 'b'), (11, 'c'), (40, 'd'), (27, 'e')]
    pq = heapq.heapify(data)    # error,   heapify is 'in-place' operation
    print(pq)                   # None
    print(data)                 # data is heapified
    while data:
        print(heapq.heappop(data))   # by default, heapify the data in ascending order



test()
