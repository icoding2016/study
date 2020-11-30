# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
# Notice that the solution set must not contain duplicate triplets.  
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# Input: nums = []
# Output: []
#
# Example 3:
# Input: nums = [0]
# Output: []
#  
# Constraints:
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

#
# "the solution set must not contain duplicate triplets".
#    -> That means, the order of the triplets dosn't matter
# The key is how to skip duplicates 


from collections import Counter


# Brutal force solution.
# T(N^3)  --  ((n-2) + (n-3) + ...1)* n * 3log3 -> O(n^3)
def sum3_bf(nums:list[int])->list[list]:
    output = []
    N = len(nums)
    if N < 3:
        return []
    for i in range(N-2):
        for j in range(i+1, N-1):
            k = 0 - nums[i] - nums[j]
            if k in nums[j+1:]:
                if sorted([nums[i],nums[j],k]) not in output:
                    output.append([nums[i],nums[j],k])
                else:
                    print('dup',[nums[i],nums[j],k].sort())
    return output


# solution2:
#   sort + approach from left / right end.
# 
# T(E^2)      E=Number of element (no dup)
def sum3_sort(nums:list[int])->list[list]:
    if len(nums) < 3:
        return []
    output = []
    counter = Counter(nums)
    sn = sorted(counter)

    if sn[0] == 0:
        if counter[0] >= 3:
            return [[0,0,0]]
        else:
            return []
    elif sn[0] > 0:
        return []

    total = 0    
    for i in range(len(sn)-1):
        if sn[i] > 0:
            break
        l = i if counter[sn[i]] > 1 else i+1
        r = len(sn)-1
        while l <= r and r < len(sn) and l < len(sn):
            if l == r and counter[sn[l]] <= 1 or \
               l == r and l == i and counter[sn[i]] < 3:
                break
            total = sn[i] + sn[l] + sn[r]
            if total == 0:
                output.append([sn[i], sn[l], sn[r]])
                l += 1
                r -= 1
            elif total < 0:
                l += 1
            else:
                r -= 1
    return output





def test_func(f):
    print(f.__name__)
    # d = [-1,0,1,2,-1,-4]
    # print(d, ' -> ', f(d))
    # d = []
    # print(d, ' -> ', f(d))
    # d = [0]
    # print(d, ' -> ', f(d))
    d = [0,0,0]
    print(d, ' -> ', f(d))
    d = [-1,0,1,0]
    print(d, ' -> ', f(d))
    d = [2,0,-4,1,-2,2]
    print(d, ' -> ', f(d))  # [[-2, 0, 2], [-4, 2, 2]]
    d = [3,0,-2,-1,1,2]
    print(d, ' -> ', f(d))  # [[-2,-1,3],[-2,0,2],[-1,0,1]]
    d = [3,0,-2,-5,1,2]
    print(d, ' -> ', f(d))  # [[-5,2,3],[-2,0,2]]




def test():
    #test_func(sum3_bf)
    test_func(sum3_sort)



test()

