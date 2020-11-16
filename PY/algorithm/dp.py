# Questions:
# 
# 8.1 Triple Step:
# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.

# 8.2 Robot in a Grid: 
# Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.
# Hints: 
#
# 8.3 Magic Index: 
# A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] =
# i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
# FOLLOW UP
# What if the values are not distinct?
# Hints:
# 
# 
# 8.4 Power Set: 
# Write a method to return all subsets of a set.
# Hints:
#   1) solution: recursive
#   2) solution: bitmap.    a smart way
#                the subsets combinitions can map to a  0101 sequence whose size=len(set), so it's just 0 ~ 2^N-1
#
# 8.5 Recursive Multiply:
# Write a recursive function to multiply two positive integers without using the
# *operator.You can use addition, subtraction, and bit shifting, but you should minimize the number
# of those operations.
# Hints: 
# 
# 8.6 Towers of Hanoi (*): 
# In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
# different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
# of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
# constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using stacks.
# Hints: #744, #224, #250, #272, #318
# 8.7 Permutations without Dups: Write a method to compute all permutations of a string of unique
# characters.
# Hints:
#   For the 3 piles(origin, buffer, dest), the disk move follows the pattern: 
#   1) move (n-1) disk from origin -> buffer
#   2) move 1 (last) disk from origin -> dest
#   3) move (n-1) disk from buffer -> dest 
# 
# 8.8 Permutations with Dups: 
# Write a method to compute all permutations of a string whose characters
# are not necessarily unique. The list of permutations should not have duplicates.
# Hints:#

# 8.9 Parens:
# Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
# of n pairs of parentheses.
# EXAMPLE
# Input: 3
# Output: ( ( () ) ) , ( () () ) , ( () ) () , () ( () ) , () () ()
# Hints: 
# 
# 8.1 O Paint Fill: 
# Implement the "paint fill" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# fill in the surrounding area until the color changes from the original color.
# Hints:
#  
# 8.11 Coins: 
# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
# pennies (1 cent), write code to calculate the number of ways of representing n cents.
# Hints:
#  
# 8.12 Eight Queens:
# Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
# so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
# diagonals, not just the two that bisect the board.
# Hints:
#  
# 8.13 Stack of Boxes: 
# You have a stack of n boxes, with widths wi , heights hi, and depths di. The boxes
# cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
# larger than the box above it in width, height, and depth. Implement a method to compute the
# height of the tallest possible stack. The height of a stack is the sum of the heights of each box.
# Hints:
# 
# 8.14 Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
# (AND), I (OR), and /\ (XOR), and a desired boolean result value result, implement a function to
# count the number of ways of parenthesizing the expression such that it evaluates to result.
# EXAMPLE
# countEval("l /\01011", false) -> 2
# countEval("0&0&0&1/\ ll0", true) -> 10
# Hints: 
#

import copy
from collections import Counter
from typing import Union, TypeVar
from call_counter import call_counter, show_call_counter


class InvalidInputException(Exception):
    pass

class Error(Exception):
    pass



# Triple Step  - find ways
# BigO:
#   T(3^n)
#   S(n*n) -- if crecord paths
#   S(n)  -- if only count without recording paths
def find_ways(n:int, total_ways:int=0, cur_path:list=None,paths:list[list]=None) -> (int, list):
    if not paths:
        paths = []
    if not cur_path:
        cur_path = []
    if n == 0:
        paths.append(cur_path.copy())
        total_ways += 1
        return total_ways, paths
    elif n == 1:
        path = cur_path + [1]  
        paths.append(path)
        total_ways += 1
        return total_ways, paths
    elif n == 2:
        path = cur_path + [1]
        total_ways, paths = find_ways(n-1, total_ways, path, paths)
        #
        path = cur_path + [2]
        paths.append(path)
        total_ways += 1
        return total_ways, paths
    else:  # >=3
        path = cur_path + [1]
        total_ways, paths = find_ways(n-1, total_ways, path, paths)
        path = cur_path + [2]
        total_ways, paths = find_ways(n-2, total_ways, path, paths)
        path = cur_path + [3]
        total_ways, paths = find_ways(n-3, total_ways, path, paths)
    return total_ways, paths


# T(3^N)
# S(N)
def count_ways(n:int) -> int:
    if n <= 1:
        return 1
    if n == 2:
        return 2
    return (count_ways(n-1) + 
            count_ways(n-2) + 
            count_ways(n-3))

# T(N)  -- On each stair, the possbility is known (the possibility sum of n-1, n-2, n-3)
# S(N)
def count_ways_memo(n:int, memo:dict=None) -> int:
    if not memo:
        memo = {}
    if n <= 1:
        memo[n]=1
        return 1
    if n == 2:
        memo[2]=2
        return 2
    if n in memo:
        return n
    
    memo[n] = (count_ways(n-1) + count_ways(n-2) + count_ways(n-3))
    return memo[n]


# Robot in a Grid
#   Top-Down
# T(2^(m+n))     -- m+n steps, each step as 2 options (binary-tree of hight=m+n), so 
# S(m+n)         -- similar to tree O(Hight)
def robot_in_grid(grid:list[list],r:int,c:int, cur_path:list[tuple]=None, paths:list[list[tuple]]=None)->list[list[tuple]]:
    if not grid or r >= len(grid) or c >= len(grid[0]):
        raise InvalidInputException()
    if paths == None:
        paths = []
    if cur_path == None:
        cur_path = [(c, r)]
    
    if r == len(grid)-1 and c == len(grid[0])-1:
        paths.append(cur_path)
        #print(cur_path)
        return paths
    if r < len(grid)-1 and grid[r][c]:       # can go down
        robot_in_grid(grid, r+1, c, cur_path + [(c, r+1)], paths)
    if c < len(grid[0])-1 and grid[r][c]:    # can go right
        robot_in_grid(grid, r, c+1, cur_path + [(c+1, r)], paths)
    return paths

# Robot in a Grid -- Memo
#   
# T(m*n)     -- each node will be covered once, and then stored in memo 
# S(m*n*(m+n))   -- each node stores the path-list at current node, and the max len of path-list is (m+n)
def robot_in_grid_memo(grid:list[list],r:int,c:int, paths_memo:dict[tuple:list[list[tuple]]]=None) -> dict[list[list[tuple]]]:
    if not grid or r >= len(grid) or c >= len(grid[0]):
        raise InvalidInputException()
    if paths_memo == None:
        paths_memo = {}
    
    if r == len(grid)-1 and c == len(grid[0])-1:
        paths_memo[(c, r)] = [[(c, r)]]
        return paths_memo

    if not grid[r][c]:    # skip
        return paths_memo
    if (c, r) in paths_memo:  # visited
        return paths_memo

    paths_memo[(c, r)] = []
    if r < len(grid)-1:       # can go down
        robot_in_grid_memo(grid, r+1, c, paths_memo)
    if c < len(grid[0])-1:    # can go right
        robot_in_grid_memo(grid, r, c+1, paths_memo)
    
    if (c, r+1) in paths_memo:
        for path in paths_memo[(c, r+1)]:
            paths_memo[(c, r)].append([(c, r)] + path)
    if (c+1, r) in paths_memo:
        for path in paths_memo[(c+1, r)]:
            paths_memo[(c, r)].append([(c, r)] + path)
    return paths_memo

# magic_index
# if the elements are distinct
# T(logN)
# S(logN)
def magic_index(A:list, l:int=None, r:int=None) -> Union[int,None]:
    if l == None:
        l = 0
    if r == None:
        r = len(A)-1
    
    if r - l == 0:      
        if A[l] == l:
            return l
        else:
            return None
    mid = l+(r-l)//2
    result = None
    if A[mid] == mid:
        return mid
    if A[mid] < mid:
        result = magic_index(A, mid+1, r)
    else:
        result = magic_index(A, l, mid)
    return result

# power set: return all subsets of a set.
# 
# T(2^N)   -- N recursive calls (N=size(S)), In each call loop size(subset)=2^N-1.  
#             But the loop size has big difference, so instead of N*(2^N-1), we add them
#             total:   (2^1-1)+(2^2-1)+...(2^N-1) -> 2^(N+1)-N -> 2^N
#             Cracking Code Interview saids it's T(N*2^N) but probably not accurate.
# S(N*2^N)   -- for each call, with current s=size(subset), it extend subset size to 2*s+1, so s(n)=s(n-1)*2+1  --> 2^N+1
#                            each set in the subset, the size is O(N).  So total    O(N*2^N)
#                            the stack: O(N), but not dominating
# Note:
#   Set() does not support indexing, but we can use pop() to pick element from it
#   Set() does not support '+', but has .add() method
#   There is one issue to fix in this solution, the full set shouldn't be includeded. 
def all_subsets(S:set, subset:list[set]=None) -> list[set]:
    if subset == None:
        subset = []
    if not S:
        return subset
    e = S.pop()
    for x in subset.copy():
        x2 = x.copy()
        x2.add(e)
        subset.append(x2)
    subset.append({e})
    all_subsets(S, subset)
    return subset

# power set: return all subsets of a set. -- bitmap implementation
# T(N*2^N)
# S(N*2^N)
def all_subsets_bitmap(S:set) -> list[set]:
    N = len(S)
    L = [x for x in S]
    output = []
    for bmap in range(1, 2**N-1):
        s = set()
        for n in range(N):
            bit = bmap & (1<<n)
            if bit:
                s.add(L[n])
        output.append(s)
    return output


# Recursive Multiply - multiply two positive integers without using the * or /
#   -- solution: adding
# T(max(a,b))
# S(max(a,b))
def recursive_multiply(a:int, b:int, result:int=0)->int:
    if a == 0 or b == 0:
        return result
    result = result + a
    return recursive_multiply(a, b-1, result)

# Multiply - multiply two positive integers without using the * or /
#   -- solution: non-recursive bit-shitting.    for a, bit n means a*2n, so bit(n)=1, then + a*2n (<<n)
# T(log(b))
# S(1)
def multiply_bitshift(a:int, b:int, result:int=0)->int:
    if a == 0 or b == 0:
        return result
    nb = b
    bitcount = 0
    while nb:
        if nb & 1:
            result += a << bitcount
        bitcount += 1
        nb = nb >> 1
    return result

# Multiply - multiply two positive integers without using the * or /
#   -- solution: non-recursive bit-shitting.    for a, bit n means a*2n, so bit(n)=1, then + a*2n (<<n)
# T(log(min(a,b)))
# S(log(min(a,b)))
def recursive_multiply_bitshift(a:int, b:int, bitpos:int=0, result:int=0)->int:
    if a == 0 or b == 0:
        return result
    if a < b:  # swap if b is bigger
        a, b = b, a
    if b & 1:
        result += a << bitpos
    bitpos += 1
    return recursive_multiply_bitshift(a, b>>1, bitpos, result)


# Towers of Hanoi -- move the disks from the first tower to the 3rd using Stacks.
#   Suppose stack s1 is ready (sorted in descending order from bottom to top), stack buffer and to are empty
#
# T(2^N):  -- each call n has 2 recursive (n-1), so the recursive calls:  1 + 2 + 2^2 + ... 2^(N-1) -> 2^N
# S(logN) ?  stack hight
#   
# Note:
#   Python's built-in list type makes a decent stack data structure as it supports push and pop operations in amortized O(1) time. 
def towers_of_hanoi(origin:list, buffer:list=None, dest:list=None, n:int=None) -> (list, list, list):
    if buffer == None:
        buffer = []
    if dest == None:
        dest = []
    if n == None:
        n = len(origin)

    if n <= 0:
        return origin, buffer, dest
    
    towers_of_hanoi(origin, dest, buffer, n-1)
    dest.append(origin.pop())
    towers_of_hanoi(buffer, origin,dest, n-1)
    return origin, buffer, dest


# Permutations without Dups:   inc. sub-string
#   Write a method to compute all permutations of a string of unique characters.
# T(N^N)    -- N=len(s),  each call: P(n) = P(n-1)*(N+2) --> O(N^N)    P(n) is the number of purmutation of str(n)
# S(N*N^N)  -- Recursive N times, each time:   P(n)*N
def str_permutations_withsub(remain:str, output:list[str]=None) -> list[str]:
    if len(remain) == 0:
        return output
    if output == None:
        output = []
    a = remain[0]
    local_output = []
    for s in output:
        for i in range(len(s)):
            local_output.append(s[:i]+a+s[i:])
        local_output.append(s+a)
    local_output.append(a)
    output.extend(local_output)
    str_permutations_withsub(remain[1:], output)
    return output


# Permutations without Dups:   not including sub-strings
# T(N!)   -- Permutation for n's call:  P(n)=P(n-1)*(n-1+1)=P(n-1)*n,  P=1 (n=1)
#                                           =1*2*3*...*n = n!
# S(N*N!)   -- Recursive call N times O(N); Buffer: P[]=P(n)=n! strings, each string O(N),  O(N*N!) 
# Note:
#   Anyway, remember the permutation of N is N!
def str_permutations(remain:str) -> list[str]:
    if len(remain) == 0:
        return []       

    local_output = []
    a = remain[0]
    perm = str_permutations(remain[1:])
    if not perm:
        local_output.append(a)
    else:
        for x in perm:
            for i in range(len(x)):
                local_output.append(x[:i]+a+x[i:])
            local_output.append(x+a)
    return local_output

# Permutations with Duplicates:
#   Since there are dup, so adding a check to skip repeat
#   compute all permutations of a string whose characters are not necessarily unique. 
#   The list of permutations should not have duplicates
# T(N!)
# S(N*N!)
def str_permutation_withdup(s:str, output:list[str]=None) -> list[str]:
    if output==None:
        output = []
    if not s:
        return output
    a = s[0]
    local_output = []
    if not output:
        local_output.append(a)
    else:
        for p in output:
            for i in range(len(p)):
                newstr = p[:i]+a+p[i:]
                if newstr in local_output:
                    continue
                local_output.append(newstr)
            newstr = p + a
            if newstr not in local_output:
                local_output.append(newstr)
    output = local_output
    return str_permutation_withdup(s[1:], local_output)

# Permutations with Duplicates:
#   optimize the dup handling by adding a flag
# T(N!)     -- worst case complexitiy is still the same O(N!),
#              but if there are many duplicate, the Counter solution is much faster. (less round of perm)
# S(N*N!)
def str_permutation_withdup_op(remain:dict, output:list[str]=None) -> list[str]:
    if output==None:
        output = []

    a = None
    for k,c in remain.items():
        if c == 0:
            continue
        remain[k] = c-1
        a = k
        break
    if a == None:
        return output
    local_output = []
    if not output:
        local_output.append(a)
    else:
        for p in output:
            for i in range(len(p)):
                newstr = p[:i]+a+p[i:]
                if newstr in local_output:
                    continue
                local_output.append(newstr)
            newstr = p + a
            if newstr not in local_output:
                local_output.append(newstr)
    output = local_output
    return str_permutation_withdup_op(remain, local_output)


# Parens: Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n pairs of parentheses.
# T(4^(n-1) ??  -- the full b-tree of 2n is T(2^2n), but there are more than half node missing in the tree. it's less than 2^n
#           O(2^n) by GeeksForGeeks, but that's quite rough
# S(n)   -- Recursive calls: 2n (For each valid str, all '(' or ')' get called once), so stack O(2n). 
#                            The call is the hight of the b-tree (2n) -> O(n)
def valid_parentheses(remain:dict, cur:str = None, output:list=None) -> list:
    if output == None:
        output = []
    if cur == None:
        cur = ''
    leftonly = False
    if remain['('] == remain[')']:
        if cur and remain[')']==0:
            output.append(cur)
            cur = ''
            return output
        leftonly = True
 
    r1 = remain.copy()
    r2 = remain.copy()
    if remain['('] > 0:
        r1['('] -= 1
        valid_parentheses(r1, cur+'(', output)
        if not leftonly:
            r2[')'] -=1
            valid_parentheses(r2, cur+')', output)    
    else:
        r2[')'] -=1
        valid_parentheses(r2, cur+')', output)    
    return output

# Paint Fill
#   Assume The image is prepresented with a list[list] M*N.
#   The colors are expressed with number 
# T(M*N)    -- recursively: visit all points, so M*N calls worst case
# S(M*N/4)  -- it's a 4-branch tree, but the routine may be Circuitous, like d,d,..d,r,r,u,u,...u,r,r,d,d.. 
#              so worst case, it's possible to be M/2 * N/2 
def paint_fill(image:list[list], x:int, y:int, color:int, old_color:int=None, marked:dict=None) -> None:
    M = len(image)
    N = len(image[0]) if image else 0
    if x < 0 or x >= N or y >= M or y < 0:
        return

    if marked == None:
        marked = {}
    if old_color == None:
        old_color = get_color(image, x, y)
        
    if (x,y) in marked:
        return
    if get_color(image, x,y) != old_color:
        return
    set_color(image, x, y, color)
    marked[(x,y)]=True

    paint_fill(image, x-1, y, color, old_color)
    paint_fill(image, x+1, y, color, old_color)
    paint_fill(image, x, y-1, color, old_color)
    paint_fill(image, x, y+1, color, old_color)
    return
    
def get_color(image:list[list], x:int, y:int) -> int:
    M = len(image)
    N = len(image[0]) if image else 0
    if x >= N or y >= M:
        raise InvalidInputException()
    return image[y][x]

def set_color(image:list[list], x:int, y:int, color:int) -> None:
    M = len(image)
    N = len(image[0]) if image else 0
    if x >= N or y >= M:
        raise InvalidInputException()
    image[y][x] = color
    return

# Coins: Given an infinite number of quarters (25 cents), dimes (1 O cents), nickels (5 cents), and pennies (1 cent), 
# write code to calculate the number of ways of representing n cents.
# T(4^N)  -- for each recursive call, there are at most 4 options. so total 1 + 4 + 4^2 + .. 4^(n-1) -> O(4^N)
# S(4N*N) -- recursive stacks: deepest is 'all 1' combination O(N), 
#            memory:  4 cur_coin objects O(N)*4 * stacks (N)
# Comment: this solution record all the combinations, which is not required for the question. need simplify to counting only
def coins_fullinfo(remain:int, cur_coins:dict=None, num_ways:int=0, ways:list[dict]=None) -> (int, list):
    if ways is None:
        ways = []
    if cur_coins == None:
        cur_coins = {25:0, 10:0, 5:0, 1:0}
    if remain == 0:
        if cur_coins not in ways:
            ways.append(cur_coins)
            num_ways += 1
        return num_ways, ways
    
    if remain >= 25:
        cur = cur_coins.copy()
        cur[25] += 1
        num_ways, ways = coins_fullinfo(remain-25, cur, num_ways, ways)
    if remain >= 10:
        cur = cur_coins.copy()
        cur[10] += 1
        num_ways, ways = coins_fullinfo(remain-10, cur, num_ways, ways)
    if remain >= 5:
        cur = cur_coins.copy()
        cur[5] += 1
        num_ways, ways = coins_fullinfo(remain-5, cur, num_ways, ways)
    if remain >= 1:
        cur = cur_coins.copy()
        cur[1] += 1
        num_ways, ways = coins_fullinfo(remain-1, cur, num_ways, ways)
    return num_ways, ways

# Coins, count ways only.
# 
# T(4^N) ? -- tree with 4 branches on each node
# S(N)    -- max hight of the tree (N)
#   
# Notice:
#   be carefull of the duplicate.
#   e.g. when iterate all the possibilities with 10, 
#        1) the coin type of sub-recursive calls shouldn't include coins >= 10 
#        2) the possibility of 10 shouldn't include 10*0, that should be covered by other smaller coin types in this round
def coins_ways_num(remain:int, coin_type:dict=None) -> int:
    if None == coin_type:
        coin_type = {25, 10, 5, 1}

    if remain == 0:
        return 1
    num_ways = 0
    for ct in coin_type:
        if remain >= ct:
            for i in range(1, int(remain/ct)+1):
                num_ways += coins_ways_num(remain-ct*i, {x for x in coin_type if x < ct})        
    return num_ways


# Coins, count ways only. with memorization
#  
# T(N)
# S(N)     -- max stack(tree) hight: O(N), each node save record O(1)
@call_counter
def coins_ways_num_memo(remain:int, coin_type:dict=None, record:dict=None) -> int:
    if None == coin_type:
        coin_type = { 25, 10, 5, 1}
    if None == record:
        record = {}    #  {<remain>:count, }
    if remain in record:
        return record[remain]
    if remain <= 0:
        if remain not in record:
            record[remain] = 1
        return 1
    total_ways = 0
    for ct in coin_type:
        if remain >= ct:
            for i in range(1, int(remain/ct)+1):
                total_ways += coins_ways_num_memo(remain-ct*i, {x for x in coin_type if x < ct})
    if remain not in record:
        record[remain] = total_ways
    return total_ways


# Eight Queens:Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
# so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
# diagonals, not just the two that bisect the board.
# 
# Solution: brutal 
#   each round (out of 8) pick 1 free position and then do the same to next position recursively.  
#   For each round, iterating all possibilities (in remaining free positions).
#   This brutal force solution takes so much time to run.  There are many duplicate in the iteration
# T(n^2n) ? -- each recursive call n*n, n level so (n*n)^n
# S(n*n)  ? -- n level of stack calls, each level use O(n) (for the new set()), so O(n*n)
def eight_queens(remain:int=8, selected:set=None, output:list=None, total:int=0)->(list,int):
    if None == selected:
        selected = set()  # {(x,y),...}
    if None == output:
        output = []       # [{<selected>}, ]

    if remain == 0:
        # check dup
        if selected not in output:
            output.append(selected)
            print(selected)
        else:
            print('skip dup..')
        return output, total 
    not_occupied = {'rows':set(range(8))-set([y for (x,y) in selected]), 
                    'cols':set(range(8))-set([x for (x,y) in selected])}
    for y in not_occupied['rows']:
        for x in not_occupied['cols']:
            if not eight_queens_is_occupied(selected,x,y):
                new_sel = selected.copy()
                new_sel.add((x,y))
                output, _ = eight_queens(remain-1, new_sel, output, total)
                total += _              
    return output, total

# Eight Queens, optimize with memorization
#  Optimization: for each round (remain), remember the combinations that have been tried. (there are many dup form diff orders)
#                skip the 'tried' combinations.
# T(n!)  -- for each 'line',T(n) = n*T(n-1) + O(n^2) -> T(n!)
#               so n'th lines -> n*(n-1)*..*1 
#               O(n^2) is the check position
#           
@call_counter
def eight_queens_memo(remain:int=8, selected:set=None, output:list=None, tried:dict=None) -> list:
    if None == output:
        output = []
    if None ==  tried:
        tried = {}
    if None == selected:
        selected = set()

    if remain == 0:
        if selected in output:
            print('skip dup..')
        output.append(selected)
        return output
    
    free_rows = set(range(8)) - set([y for (x,y) in selected])
    free_cols = set(range(8)) - set([x for (x,y) in selected])
    for y in free_rows:
        for x in free_cols:
            if not eight_queens_is_occupied(selected, x, y):
                new_selected = selected.copy()
                new_selected.add((x,y))
                if remain in tried:
                    if new_selected in tried[remain]:   # tried combination, skip
                        continue
                    else:
                        tried[remain].append(new_selected)
                else:
                    tried[remain] = [new_selected]
                eight_queens_memo(remain - 1, new_selected, output, tried)
    return output

# Eight Queens,
#  simplify data struct for board.  (8*8 matrix -> rows[y]=x), much more faster
# 
# T(n!)  -- for each 'line',T(n) = n*T(n-1) + O(n^2) -> T(n!)
#               so n'th lines -> n*(n-1)*..*1 
#               O(n^2) is the check valid position (eight_queens2_check_occupied)
# S(n*n) or S(n)  -- call stack: max n level O(n), if consider each level has temp arg of size(n), then O(n*n) 
@call_counter
def eight_queens2(remain:int=8, rows:list=None, output:list=None) -> list:
    if None == rows:
        rows = []
    if None == output:
        output = []

    if remain == 0:
        output.append(rows)
        #print(rows)
        return output
    for col in range(8):
        if not eight_queens2_check_occupied(rows, 8-remain, col):
            #rows.append(col)
            eight_queens2(remain-1, rows+[col], output)
    return output

def eight_queens2_check_occupied(rows:list, row:int, col:int):
    if row in range(len(rows)):
        return True
    if col in rows:
        return True
    occupied_list = [(rows[r],r) for r in range(len(rows))]
    for i in range(8):
        if (col - i >= 0 and row - i >= 0 and (col-i, row-i) in occupied_list) or \
           (col + i < 8 and row + i < 8 and (col+i, row+i) in occupied_list) or \
           (col - i >= 0 and row + i < 8 and (col-i, row+i) in occupied_list) or \
           (col + i < 8 and row - i >=0 and (col+i, row-i) in occupied_list):
            return True   # occupied
    return False
    

def eight_queens_is_occupied(occupied_list:set, x:int, y:int) -> bool:  # True = occupied
    rows = [y for (x,y) in occupied_list]
    cols = [x for (x,y) in occupied_list]
    if x in cols or y in rows:
        return True
    for i in range(8):
        if (x - i >= 0 and y - i >= 0 and (x-i, y-i) in occupied_list) or \
           (x + i < 8 and y + i < 8 and (x+i, y+i) in occupied_list) or \
           (x - i >= 0 and y + i < 8 and (x-i, y+i) in occupied_list) or \
           (x + i < 8 and y - i >=0 and (x+i, y-i) in occupied_list):
            return True   # occupied
    return False



# Stack of Boxes
#  ? don't understand the question



# Boolean Evaluation: 
# Given a boolean expression consisting of the symbols 0(false), 1(true), &(AND), I(OR), and /\ (XOR), 
# and a desired boolean result value result, 
# implement a function to count the number of ways of parenthesizing the expression such that it evaluates to result
# EXAMPLE
#   countEval("l/\0|0|1", false) -> 2
#   countEval("0&0&0&1All0", true)-> 10
# Idea:
# 1) Brutal force
#   The pattern is  (exp-left) <opr> (exp-right)
#   desired-result  opr: 
#    True            &      left-True/right-True
#                    |      left-True/right-True, left-True/right-False, left-False/right-True
#                    ^      left-True/right-False, left-False/right-True
#    False           &      left-True/right-False, left-False/right-True, left-False/right-False
#                    |      left-False/right-False
#                    ^      left-True/right-True, left-False/right-False
# 
# T(N^N) ?  --  the call has  N/2(oprs) * 4 recursions,
#    the 1st level recursion: N/4
#
@call_counter
def count_evals(expression:str, desired:bool) -> int:
    if not expression:
        return 0
    if len(expression) == 1:
        ret = 1 if (expression == ('1' if desired else '0')) else 0
        #print('{} {} -> {}'.format(expression, desired, ret))
        return ret
    if len(expression) == 2:
        raise InvalidInputException('expression too short: {}'.format(expression))
    
    count = 0
    for i in range(1, len(expression), 2):
        left = expression[:i]
        opr = expression[i]
        right = expression[i+1:]
        #print('({}){}({})'.format(left, opr, right))
        left_true = count_evals(left, True)       #; print('{} True ->{}'.format(left, left_true))
        left_false = count_evals(left, False)     #; print('{} False ->{}'.format(left, left_false))
        right_true = count_evals(right, True)     #; print('{} True ->{}'.format(right, right_true))
        right_false = count_evals(right, False)   #; print('{} False ->{}'.format(right, right_false))
        if desired:
            if opr == '&':
                count += left_true * right_true
            elif opr == '|':
                count += left_true * right_true + left_true * right_false + left_false * right_true
            else:  # '^'
                count += left_true * right_false + left_false * right_true
        else:
            if opr == '&':
                count += left_true * right_false + left_false * right_true + left_false * right_false
            elif opr == '|':
                count += left_false * right_false
            else:  # '^'
                count += left_true * right_true + left_false * right_false
    return count

@call_counter
def count_evals_memo(expression:str, desired:bool, memo:dict=None) -> int:
    if None == memo:
        memo = dict()
    if not expression:
        return 0
    if len(expression) == 1:
        ret = 1 if (expression == ('1' if desired else '0')) else 0
        return ret
    if len(expression) == 2:
        raise InvalidInputException('expression too short: {}'.format(expression))
    
    if (expression, desired) in memo:
        return memo[(expression, desired)]

    count = 0
    for i in range(1, len(expression), 2):
        left = expression[:i]
        opr = expression[i]
        right = expression[i+1:]
        #print('({}){}({})'.format(left, opr, right))
        left_true = count_evals_memo(left, True, memo)       #; print('{} True ->{}'.format(left, left_true))
        left_false = count_evals_memo(left, False, memo)     #; print('{} False ->{}'.format(left, left_false))
        right_true = count_evals_memo(right, True, memo)     #; print('{} True ->{}'.format(right, right_true))
        right_false = count_evals_memo(right, False, memo)   #; print('{} False ->{}'.format(right, right_false))
        if desired:
            if opr == '&':
                count += left_true * right_true
            elif opr == '|':
                count += left_true * right_true + left_true * right_false + left_false * right_true
            else:  # '^'
                count += left_true * right_false + left_false * right_true
        else:
            if opr == '&':
                count += left_true * right_false + left_false * right_true + left_false * right_false
            elif opr == '|':
                count += left_false * right_false
            else:  # '^'
                count += left_true * right_true + left_false * right_false
    
    memo[(expression,desired)]=count
    return count




def test():

    print("find_ways")
    n = 4
    c, paths = find_ways(n)
    print('Total possibilities for {} stairs: {} '.format(n, c))
    for path in paths:
        print(path)

    n = 5
    print('Total possibilities for {} stairs: {} '.format(n, count_ways(n)))
    print('Count ways memo for {} stairs: {} '.format(n, count_ways_memo(n)))

    # robot_in_grid
    grid = [[1,1,1,1,0,1],
            [1,0,1,0,1,1],
            [1,1,1,1,1,0],
            [1,0,1,0,1,1],
           ]
    print('robot_in_grid:')
    for path in robot_in_grid(grid, 0, 0):
        print(path)
    print('robot_in_grid_memo:')
    paths_memo = robot_in_grid_memo(grid, 0, 0)
    if (0, 0) in paths_memo:
        for path in paths_memo[(0,0)]:
            print(path)


    # magic_index
    print('magic_index')
    a = [-40,-20,-1,1,2,3,5,7,9,12,13]
    print('{} -> {}'.format(a, magic_index(a)))    # 7
    a = [-40,-20,-1,1,2,3,5,6,7,8,12,13]
    print('{} -> {}'.format(a, magic_index(a)))    # None

    # all_subsets
    print('all_subsets')
    s = all_subsets({1,2,3,4})
    print(s, 'count:', len(s))
    s = all_subsets_bitmap({1,2,3,4})
    print(s, 'count:', len(s))

    # recursive_multiply
    print('recursive_multiply')
    print("{}*{}={}".format(3, 4, recursive_multiply(3,4)))
    print("{}*{}={}".format(0, 5, recursive_multiply(0,5)))
    print("{}*{}={}".format(2, 15, recursive_multiply(2,15)))
    print("{}*{}={}".format(4, 0, recursive_multiply_bitshift(4, 0)))
    print("{}*{}={}".format(3, 15, recursive_multiply_bitshift(3,15)))
    print("{}*{}={}".format(30, 5, recursive_multiply_bitshift(30,5)))

    # towers_of_hanoi
    s1 = [10,9,8,7,6,5,4,3,2,1]
    s1, s2, s3 = towers_of_hanoi(s1)
    print('s1:',s1)
    print('s2:',s2)
    print('s3:',s3)

    # str_permutations_withsub
    s = 'abc'
    print('str_permutations_withsub: {}'.format(s))
    p = str_permutations_withsub(s)
    print(p)
    print('total: ', len(p))

    print('str_permutations: {}'.format(s))
    p = str_permutations(s)
    print(p)
    print('total: ', len(p))

    print('str_permutations_withdup')
    print(str_permutation_withdup('abb'))
    c = Counter('abb')
    print('str_permutations_withdup_op')
    print(str_permutation_withdup_op(c))

    # valid_parentheses
    print('valid_parentheses')
    n = 3
    d = {'(':n, ')':n}
    print(valid_parentheses(d))

    # paint_fill
    image = [[2,2,1,1,2,1,5,4,1,1], 
             [1,2,2,1,1,1,1,4,4,2],
             [1,2,5,5,1,4,4,4,2,2],
             [5,1,1,4,1,4,4,1,2,2],
             [4,5,5,1,1,1,1,1,1,1],
            ]
    color = 0
    x = 4
    y = 1
    for line in image:
        print(line)
    print("paint_fill to {} at ({},{})".format(color, x, y))
    paint_fill(image, x, y, color)
    for line in image:
        print(line)

    # coins
    n = 34
    print('coins_fullinfo for ', n)
    print(coins_fullinfo(n))
    print('coins_ways_num for ', n)
    print(coins_ways_num(n))
    print('coins_ways_num_memo for ', n)
    print(coins_ways_num_memo(n))
    print(show_call_counter())
    
    # eight_queens
    print('eight_queens')
    #output, total = eight_queens()
    #print('tried:', total)
    #output = eight_queens_memo()   # run long time > 10min
    # print(show_call_counter())
    # print(output)
    # for solution in output:
    #     print('_'*30)
    #     for y in range(8):
    #         for x in range(8):
    #             if (x,y) in solution:
    #                 print('1 ',end='')
    #             else:
    #                 print('0 ', end='')
    #         print('')
    # print('available solutions:', len(output))

    output = eight_queens2()
    for rows in output:
        print("="*16)
        for r in range(8):
            col = rows[r]
            print('- '*(col) + 'x ' + '- '*(7-col))
    print(show_call_counter())
    print('solutions: {}'.format(len(output)))

    # count_evals
    print('count_evals')
    s = '1^0|0|1'; d=False
    print('{},{} -> {}'.format(s, d, count_evals(s,d)))
    s = '0&0&0&1^1|0'; d=True
    print('{},{} -> {}'.format(s, d, count_evals(s,d)))
    print(show_call_counter())

    print('count_evals_memo')
    s = '1^0|0|1'; d=False
    print('{},{} -> {}'.format(s, d, count_evals_memo(s,d)))
    s = '0&0&0&1^1|0'; d=True
    print('{},{} -> {}'.format(s, d, count_evals_memo(s,d)))
    print(show_call_counter())


test()
