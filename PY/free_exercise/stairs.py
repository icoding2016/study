# go up stair with 1/2/3 stairs_ways-hop each time, how many ways to reach the top (stair N)




# T(3^n)  -- for each stair, 3 ways to hop.   O() = 3*3*..3 = 3^n
def stairs_ways(remain:int, path:list=None)->None:
    if None == path:
        path = []
    
    if remain < 0:
        return
    if remain == 0:
        yield path
    
    if remain == 1:
        yield path+[1]
    elif remain == 2:
        yield path+[1,1]
        yield path+[2]
    else:
        for x in stairs_ways(remain-1, path+[1]):
            yield x
        for x in stairs_ways(remain-2, path+[2]):
            yield x
        for x in stairs_ways(remain-3, path+[3]):
            yield x
    return    


# Counting for the ways.  DP
# T(n)
# S(n)
def stairs_way_count(remain:int)->int:
    ways = [0 for i in range(remain+1)]      # index: stair, ways[index]=ways
    ways[0],ways[1],ways[2],ways[3] = 0,1,2,4
    for i in range(4, remain+1):
        ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
    return ways[remain]

    


def test():
    total = 0
    n = 4
    for p in stairs_ways(n):
        print(p)
        total += 1
    print('stairs_ways:', total)
    print('stairs_way_count:', stairs_way_count(n))



test()

