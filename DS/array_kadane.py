"""
Largest Sum Contiguous Subarray (via Kadane’s Algorithm)
Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum.

The idea of Kadane’s algorithm is to maintain a variable max_ending_here that stores the maximum sum contiguous subarray ending at current index
  and a variable max_so_far stores the maximum sum of contiguous subarray found so far, 
  Everytime there is a positive-sum value in max_ending_here compare it with max_so_far and update max_so_far if it is greater than max_so_far.

At each position (i), the max_sub[i] = max(max_sub[i-1], a[i])

Kadane's algorithm has a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array. 

"""

import random
import typing as t

N=20
A = [random.randint(-100,100) for i in range(N)]
A_override = [-81, 70, -86, 25, -88, 64, -32, 40, -1, -99, -17, -10, -9, -92, 76, 49, 17, 14, -6, 70]


# T(N^3)
#    Rouphly, N*N*N  (i, j, sum())
#    MorePrecise, (N-1)^2+(N-2)^2+...+1 = N(N+1)(2N+1)/6 => N^3
# S(N^2), 
#    In the worst case, if every subarray is distinct and considered large, the space complexity would be O(n^2),
#    where n is the length of the input list a.
def LargestContinuousSub(a:list) -> t.Tuple[t.List, int]:
    large_arr=[]
    large_sum=None 
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            s = sum(a[i:j+1])
            if not large_sum or s > large_sum:
                large_arr = [a[i:j+1]]
                large_sum = s
            elif s == large_sum:
                large_arr.append(a[i:j+1])
    return (large_arr, large_sum)            


# T(N)
# S(1)
def kadane(a:list) -> t.Tuple[t.List, int]:
    largest_sub_start = largest_sub_end = 0
    largest_sum = a[0]
    for i in range(1, len(a)):
        if a[i] > largest_sum + a[i]:
            largest_sub_start = largest_sub_end = i
            largest_sum = a[i]
        else:
            largest_sub_end = i
            largest_sum = largest_sum + a[i]
    
    return (a[largest_sub_start:largest_sub_end+1], largest_sum)


# T(N)
# S(N^2)  the largest_sub stores N substring whose size could be N in worst case
#         We can simply use a O(N) space to record current largest sub 
#         or O(1) to record the pos of start/end.
def kadane_bad_space_complexity(a:list) -> t.Tuple[t.List, int]:
    largest_sub = [None for i in range(len(a))]    # largest_sub at i
    largest_sum = [None for i in range(len(a))]
    largest_sub[0] = [a[0]]
    largest_sum[0] = a[0]
    for i in range(1, len(a)):
        if a[i] > largest_sum[i-1] + a[i]:
            largest_sub[i] = [a[i]]
            largest_sum[i] = a[i]
        else:
            largest_sub[i] = largest_sub[i-1] + [a[i]]
            largest_sum[i] = largest_sum[i-1] + a[i]
    
    large_pos = 0
    for i in range(len(largest_sum)):
        if largest_sum[i] > largest_sum[large_pos]:
            large_pos = i
    return (largest_sub[large_pos], largest_sum[large_pos])


def test():
    a = A_override if A_override else A
    print(f"A: {a}")
    large_arr, large_sum = LargestContinuousSub(a)
    print(f"by LargestContinuousSub:\n{large_arr}, {large_sum}")
    large_arr, large_sum = kadane(a)
    print(f"by Kadane:\n{large_arr}, {large_sum}")


test()