"""
“Dutch National Flag problem”

Given an array A[] consisting of only 0s, 1s, and 2s. 
The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.

Or 'sort color balls' question:
Given N balls of colour red, white or blue arranged in a line in random order.
You have to arrange all the balls such that the balls with the same colours are adjacent with the order of the balls,
  with the order of the colours being red, white and blue.

Dutch National Flag solution:
- The problem is similar to “Segregate 0s and 1s in an array”.
- The problem was posed with three colors, here `0′, `1′ and `2′. The array is divided into four sections: 
  arr[1] to arr[low – 1]
  arr[low] to arr[mid – 1]
  arr[mid] to arr[high – 1]
  arr[high] to arr[n]
- If the ith element is 0 then swap the element to the low range.
- Similarly, if the element is 1 then keep it as it is.
- If the element is 2 then swap it with an element in high range.


"""


from collections import Counter
from random import randint


N = 15  # size
A = [randint(0,2) for i in range(N)]


# T(N),  O=max(N, ClogC), the loop is O(N), sort is Clog(C) (C=3 in this example) and it's a constent
# S(N),  4xN space
def sort_012_array_counter(a: list) -> list:
    count = Counter(a)
    result = []
    keys = sorted(count.keys())
    for v in keys:
        result += [v for i in range(count[v])]
    return result


# T(N)   max(N, Clog(C))
# S(N)
def sort_012_array_bucket(a: list) -> list:
    buckets = {i:[] for i in set(a)}
    for v in a:
        buckets[v].append(v)
    result = []
    for v in sorted(set(a)):
        result += buckets[v]
    return result


# T(N)
# S(N)
def dutch_national_flag(a: list) -> list:
    low = mid = 0
    high = len(a) - 1
    while mid <= high and mid < len(a):
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]     # swap mid/low
            low += 1
            if mid < low:
                mid += 1
        elif a[mid] == 2:
            a[high], a[mid] = a[mid], a[high]     # swap mid/low
            high -= 1
        else:
            mid += 1
    return a


def test():
    a = A
    print(f"Input array: {a}")
    result = sort_012_array_counter(a)
    print(f"sort_012_array_counter result: {result}")
    result = sort_012_array_bucket(a)
    print(f"sort_012_array_bucket result: {result}")
    result = dutch_national_flag(a)
    print(f"dutch_national_flag result: {result}")

test()
