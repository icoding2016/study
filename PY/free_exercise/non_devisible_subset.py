# non-divisible-subset
# https://www.hackerrank.com/challenges/non-divisible-subset/problem
#
# Given a set of distinct integers, print the size of a maximal subset of S -- max len(S')
# where the sum of any 2 numbers in S' is not evenly divisible by k.
# For example, the array [19,10,12,10,24,25,22] and k=4. 
# One of the arrays that can be created is [10,12,25]. Another is [19,22,24]. 
# After testing all permutations, the maximum length solution array has 3 elements.
#
# Function Description
# Complete the nonDivisibleSubset function. 
# It should return an integer representing the length of the longest subset of  meeting the criteria.
#
# nonDivisibleSubset has the following parameter(s):
# S: an array of integers
# k: an integer
#
# Constraints
#  - 1<=n<=10^5
#  - k<=k<=100
#  - 1<=S[i]<=10^9
#  - All of the given numbers are distinct
# Output Format
#  Print the size of the largest possible subset ().

# Sample Input
# 3, [1,7,2,4]
# Sample Output
# 3
# Explanation
# The sums of all permutations of two elements from  are:
# 1 + 7 = 8
# 1 + 2 = 3
# 1 + 4 = 5
# 7 + 2 = 9
# 7 + 4 = 11
# 2 + 4 = 6
# We see that only S'=[1,7,4] will not ever sum to a multiple of k=3.





def nonDivisibleSubset(k, s):
    # Write your code here
    return process(k,s)

def process(k,s,mx=0, cur=None, memo=None):
    if None == cur:    
        cur = []
    if None == memo:
        memo = {}
    if k <= 1:
        return 0
    if not s:
        if (len(cur)==1 and cur[0]%k!=0) or len(cur)>1:            
            if len(cur)>mx:
                mx=len(cur)
        return mx
    
    cur.sort()
    if tuple(cur) in memo:
        return memo[tuple(cur)]
    n = s[0]
    if not cur or not any([(c+n)%k==0 for c in cur]):
        mx = process(k,s[1:], mx, cur+[n])
    mx = process(k,s[1:], mx, cur)
    memo[tuple(cur)]=mx
    return mx            

def process0(k,s,cur=None, output=None)->list:
    if None == output:    
        output = []
    if None == cur:    
        cur = []
    if not s:
        if cur not in output and \
           not (len(cur) == 1 and cur[0]%k==0):            
            output.append(cur)
        return output
    
    n = s[0]
    if not cur or not any([(c+n)%k==0 for c in cur]):
        process(k,s[1:], cur+[n], output)
    process(k,s[1:], cur, output)
    return output            


def test_fixture():
    testdata = [  # (input, expect),
        ((3, [1,7,2,4,]), 3),
        ((1, [1,7,2,4,]), 0),
        ((4, [19,10,12,10,24,25,22]), 3),
        ((7, [278,576,496,727,410,124,338,149,209,702,282,718,771,575,436]),11),
        ((3, [3]), 0),
        ((3, [4]), 1),
        ((5, [x for x in range(1,31)]), 13),
        #((3, [x for x in range(1,101)]), 35),
    ]

    for i in range(len(testdata)):
        ret = nonDivisibleSubset(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))


import timeit
def test():
    #s = Solution()
    test_fixture()

test()
# timeit.timeit('test()', number=1)    
