# n-choose-k problem:  choose k xx from n xx, 
# permutation: order matters
# combination: order doesn't matter
#
# Recursive Solution: C(n,k)=C(n-1,k-1) + C(n-1,k) 
# If simply counting, can use math solution:   C(n,k)= n!/((n-k)!*k!)


# Typical Question: There are N marbles with different colors, pick k, how many combinations
# There are 2 cases:  1) color has no duplications 
#                     2) color has duplications
#  represent color with number 
from call_counter import call_counter, show_call_counter


# Counting only
@call_counter
def n_choose_k_count_recursive(n:int, k:int)->int:
    if k==0 or k==n:
        return 1
    return n_choose_k_count_recursive(n-1, k-1) + n_choose_k_count_recursive(n-1, k)

def n_choose_k_count_factorial(n, k):
    return int(fact(n)/(fact(n-k)*fact(k)))

def fact(n):
    if n <= 1:
        return 1
    return fact(n-1)*n


# Combination
#   solution for duplicates: check & skip.
#     note: it's not easy to compare lists (order matters), so we can use set() in this case
@call_counter
def n_choose_k_nodup(remain:set, k:int, cur:set=None, output:list=None)-> (int, list):
    if None == cur:
        cur = set()
    if None == output:
        output = []
    
    # base case of the recursion
    if k == 0:
        # soluton1 for dup:  check dup
        if cur in output: 
            return (0, output)
        output.append(cur)
        return (1, output)
    if k == len(remain):
        cur = cur.union(remain)
        if cur in output: 
            return (0, output)
        output.append(cur)
        return (1, output)

    total = 0
    for x in remain:
        t, _ = n_choose_k_nodup(remain-set([x]), k-1,  set.union(cur,set([x])), output)    # note: cur.copy() to avoid impacting other routings
        total += t
    return total, output


# The key issue is 'how to avoid duplicate'  (well checking the existing combination is simple but not effecient)
#   Solution for duplications: remember the picked elements and skip them in the rest of the iterations.
#                              This is similar to marking a vertex as 'visited' in graph traversal.
#   The solution is more efficient than above (checking solution)
# T(n^2)   -- for each iteration: O(n-1), so total (n-1)+(n-2)+..1=n*(n-1)/2
@call_counter
def n_choose_k_nodup2(remain:set, k:int, cur:list=None, output:list=None)-> (int, list):
    # init
    if None == output:
        output = []
    if None == cur:
        cur = []

    # base base
    if k == 0:
        output.append(cur)
        return 1, output
    if k == len(remain):
        output.append(cur+[x for x in remain])
        return 1, output

    count = 0
    picked = set()
    for x in remain:
        picked.add(x)            # remember the used one (with full combinations), skip it in the rest iteration
        c, _ = n_choose_k_nodup2(remain-picked, k-1, cur + [x], output)
        count += c
    return count, output


def test():
    n = 10; k = 3
    print(n_choose_k_count_factorial(n, k))
    print(n_choose_k_count_recursive(n, k))
    show_call_counter()

    data = [1,2,3,4]
    print(n_choose_k_nodup(set(data), 3))
    show_call_counter()

    t, output = n_choose_k_nodup2(set(data), 3)
    print('total: ', t)
    print(output)
    show_call_counter()


test()
