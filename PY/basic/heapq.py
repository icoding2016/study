import heapq

def test():
    data = [(30, 'a'), (25, 'b'), (11, 'c'), (40, 'd'), (27, 'e')]
    print('original data: ', data)

    hq1 = data[:]
    pq = heapq.heapify(hq1)    # error,   heapify is 'in-place' operation
    print(pq)                   # None
    print(hq1)                 # data is heapified

    while hq1:
        print(heapq.heappop(hq1))   # by default, heapify the data in ascending order

    hq = []
    #heapq.heapify(hq)
    for d in data:
        heapq.heappush(hq, d)
    print(hq)

test()
