# Solve the Hanoi Tower problem
# given 3 towers, move all disks from tower1 to tower2


# suppose each round of call partially solves the piles,  src:(n-i), dst:i, temp:0
# The operation pattern: (say n disks in src)
#   1) move n-1 disks from src to temp
#   2) move 1 (last) disk from src to dst
#   3) move n-1 disks from temp to dst
#  
# Time complexity:
#   for each 'n' disks,  we need 3 steps to solve (n-1) disks. 
#   So  step(n)=2*steps(n-1)+1,   O(n) = 2*O(n-1)+1 = 2(2*O(n-2)+1) = ... 2^n
#     


from collections import defaultdict

# T(2^n)
def hanoi(remain:int, src:list, dst:list, temp:list)->int:
    if remain <= 0:
        return 0

    steps = 0
    steps += hanoi(remain-1, src, temp, dst)
    dst.append(src.pop())
    steps += 1
    steps += hanoi(remain-1, temp, dst, src)
    return steps


def hanoi_steps(remain:int, memo:dict=None)->int:
    if None == memo:
        memo = defaultdict(int)
    memo[1] = 1
    for i in range(1,remain+1):
        memo[i] = 2*memo[i-1]+1
    return memo[remain]




def test():
    n = 10
    s = [x for x in range(n, 0, -1)]
    d = []*len(s)
    t = []*len(s)
    print(s, '->')
    print('steps: ', hanoi(len(s), s, d, t))
    print(s)
    print(d)
    print(t)

    print('hanoi_steps for {} disk: {}'.format(n, hanoi_steps(n)))

test()
