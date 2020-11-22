# Leetcode: Unique Paths  Medium
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
# e.g.
#   Input: m = 3, n = 7,  Output: 28 

 
from call_counter import call_counter, show_call_counter

############### Count only ###############
# T(2^(m+n))  ??
# S(m+n)      ??
@call_counter
def unique_path_count_recursive(m:int, n:int)->int:
    if m == 1 and n == 1:        
        return 1
    count = 0
    if n > 1:
        count += unique_path_count_recursive(m, n-1)
    if m > 1:
        count += unique_path_count_recursive(m-1, n)
    return count

@call_counter
# T(m*n)
# S(m*n)
def unique_path_count_recursive_dp(m:int, n:int, memo:dict=None)->int:
    if None == memo:
        memo = dict()
    if m == 1 and n == 1:        
        return 1
    if (m,n) in memo:
        return memo[(m,n)]
    count = 0
    if n > 0:
        count += unique_path_count_recursive_dp(m, n-1, memo)
    if m > 0:
        count += unique_path_count_recursive_dp(m-1, n, memo)
    memo[(m,n)] = count
    return count


############### Count & paths ###############
# Find all paths from left top to bottom right

@call_counter
def unique_paths_recursive(m:int, n:int, cur:list=None, paths:list=None)->(int,list):
    if None == cur:
        cur = [(m, n)]
    if None == paths:
        paths = []
    if m == 1 and n == 1:        
        paths.append(cur)
        return 1, paths
    count = 0
    if n > 0:
        count, _ = unique_paths_recursive(m, n-1, cur + [(m, n-1)], paths)
    if m > 0:
        c2, _ = unique_paths_recursive(m-1, n, cur + [(m-1, n)], paths)
        count += c2
    return count, paths


# Find all the paths from top-left to bottom-right
# T(m*n)        ?
# S(m*n*(m+n))  ?
@call_counter
def unique_paths_dp(m:int, n:int)->(int,list):
    memo = dict()
    memo[(1,1)] = [[(1,1)],]
    for y in range(1, m+1):
        for x in range(1, n+1):
            if (x,y) not in memo:
                if x > 1:
                    memo[(x,y)] = [p+[(x,y)] for p in memo[(x-1,y)]]
                if y > 1:
                    if (x,y) in memo:
                        memo[(x,y)].extend([p+[(x,y)] for p in memo[(x, y-1)]])
                    else:
                        memo[(x,y)] = [p+[(x,y)] for p in memo[(x,y-1)]]
    return len(memo[(n,m)]), memo[(n, m)]


def test():
    m = 3
    n = 3
    print(unique_path_count_recursive(m, n))
    show_call_counter()
    print(unique_path_count_recursive_dp(m, n))
    show_call_counter()

    print(unique_paths_recursive(m,n))
    show_call_counter()

    #print(unique_paths_recursive_memo(m,n))
    print(unique_paths_dp(m,n))
    show_call_counter()


test()
