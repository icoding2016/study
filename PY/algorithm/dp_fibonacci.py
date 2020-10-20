# DP (Dynamic Programming)
#   The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later.
#
# Fibonacci:  f(n)=f(n-1)+f(n-2)

import timeit

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_dp(n):
    F = [0, 1]
    fn = 0
    for i in range(2,n+1):
        fn = F[i-1] + F[i-2]
        F.append(fn)
    return fn

def test():
    n = 10
    print(fibonacci(n))
    print(fibonacci_dp(n))


test()




