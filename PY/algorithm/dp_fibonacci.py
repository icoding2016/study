# DP (Dynamic Programming)
#   The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later.
#
# Fibonacci:  f(n)=f(n-1)+f(n-2)

import timeit

# Time Complexity:  O(2^n)   -- the recursive call of f(n) is 1 + 2 + 2^2 + 2^3 ... 2^(n-1)
# Space Complexity: O(n)   !!
#     Note: SC may be mistaken to O(2^n) -- O(1) space for each recursive stack and there are O(2^n) recursive call
#           But in fact the calls are made in the way as a B-Tree Depth-First-Search. So the max hight of stack is just n, 
#     ref: https://www.youtube.com/watch?v=dxyYP3BSdcQ 
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# Bottom-Up DP
# Time Complexity:  O(n)
# Space Complexity: O(n)
def fibonacci_dp(n):
    F = [0, 1]
    fn = 0
    for i in range(2,n+1):
        fn = F[i-1] + F[i-2]
        F.append(fn)
    return fn

# Top-Down DP
# Time Complexity:  O(2n) -> O(n)
# Space Complexity: O(n) -- the max hight of call stack
def fibonacci_memo(n:int, memo:dict = None) -> int:
    if not memo:
        memo = {}
    if n < 2:
        memo[n] = n
        return n

    if n not in memo:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2,memo)
    return memo[n]

def test():
    n = 10
    print(fibonacci(n))
    print(fibonacci_dp(n))
    print(fibonacci_memo(n))


test()




