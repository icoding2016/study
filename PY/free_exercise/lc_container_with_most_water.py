# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/ 
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
#              In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
# Input: height = [1,1]
# Output: 1
#
# Example 3:
# Input: height = [4,3,2,1,4]
# Output: 16
#  
# Example 4:
# Input: height = [1,2,1]
# Output: 2

# Constraints:
# n = height.length
# 2 <= n <= 3 * 104
# 0 <= height[i] <= 3 * 104
 

# T(N^N)  -- (n-1) + (n+2) + ...1 =  n(n+1)/2
# S(1)
def most_water_bf(data:list[int])->(int,tuple):
    N = len(data)
    max_contain = 0
    result = (0,0)
    for i in range(N-1):
        for j in range(i+1, N):
            contain = (j-i)*min(data[i], data[j])
            if max_contain < contain:
                max_contain = contain
                result = (i, j)
    return (max_contain, result)

# T(N)
def most_water_tocenter(data:list[int])->(int,tuple):
    start = 0
    end = len(data) - 1
    max_contain = 0
    result = (0,0)
    flag = True
    while end > start:
        contain = min(data[end], data[start])*(end-start)
        if contain > max_contain:
            max_contain = contain
            result = (start, end)
            flag = False if flag else True
        if flag:
            end -= 1
        else:
            start += 1
    return (max_contain, result)



def test_func(f):
    print(f.__name__)
    d = [1,8,6,2,5,4,8,3,7]
    print(d, ' -> ', f(d))   # 49
    d = [1,1]
    print(d, ' -> ', f(d))   # 1
    d = [4,3,2,1,4]
    print(d, ' -> ', f(d))   # 16
    d = [1,2,1]
    print(d, ' -> ', f(d))   # 2


def test():
    test_func(most_water_bf)
    test_func(most_water_tocenter)


test()


