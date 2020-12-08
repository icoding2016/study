# Coin Change 2
# Medium
# You are given coins of different denominations and a total amount of money. 
# Write a function to compute the number of combinations that make up that amount.
#  You may assume that you have infinite number of each kind of coin.
#
# Example 1:
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# 
# Example 3:
# Input: amount = 10, coins = [10] 
# Output: 1
# 
# Note:
# You can assume that
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
#

from typing import List
from collections import defaultdict


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # n = self.change_recursive(amount, coins)
        #n = self.change_recursive_memo(amount, coins)
        n = self.change_dp(amount, coins)
        return n

    # T(N^(amount/coin_min))    N - num of coins
    # S(max(len(coin), amount/min_c))
    def change_recursive(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if amount < 0 or len(coins)==0:
            return 0
        c = coins[0]
        n1 = self.change_recursive(amount-c, coins[:])
        n2 = self.change_recursive(amount, coins[1:])
        return n1+n2

    def change_recursive_memo(self, amount: int, coins: List[int], memo:dict=None) -> int:
        if memo == None:
            memo = defaultdict(int)
        if amount == 0:
            return 1
        if amount < 0 or len(coins)==0:
            return 0
        if (amount, tuple(coins)) in memo:
            return memo[(amount, tuple(coins))]
        c = coins[0]        
        n1 = self.change_recursive_memo(amount-c, coins[:], memo)
        n2 = self.change_recursive_memo(amount, coins[1:], memo)
        memo[(amount, tuple(coins))] = n1+n2
        return n1+n2


    # N(amount) = sum([N(amount-c) for c in coins])
    # This gives wrong output because some duplicates solutions are counted if we loop amount first, then coins.
    #   e.g   amount 0,   1,   2,   3,   4
    #      coin 1    1    1    1    1    1
    #                     '+1-> '+1->
    #                '-- +2 --> '+1->
    #                     '-- +2 -->   
    #      coin 2    1         2    3 
    #                               ^____________ the 3 is wrong because it count (1,1,1), (1,2), (2,1) where (2,1) duplicate
    #      coin 5    1
    #  see https://leetcode.com/problems/coin-change-2/discuss/176706/Beginner-Mistake%3A-Why-an-inner-loop-for-coins-doensn't-work-Java-Soln
    # # 
    def change_dp_wrong(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(int)
        coins.sort()
        dp[0] = 1
        a = min(coins) if coins else 0
        while a <= amount:             
            num = 0
            for c in coins:
                if a-c in dp:
                    num += dp[a-c]
            dp[a] = num
            a += 1
        print(dp)
        if amount in dp:
            return dp[amount]
        else:
            return 0

    # N(amount) = sum([N(amount-c) for c in coins])
    #  correct the loop: loop coins first, then amount
    #   e.g   amount 0,   1,   2,   3,   4,   5
    #      coin 1    1    1    1    1    1    1
    #                     '+1->'+1->'+1-> '+1->
    #      coin 2    1    1    2    2    3    3
    #                '-- +2 --> '-- +2 --> '-- +2 -->
    #                     '-- +2 -->'-- +2 -->
    #      coin 5    1                        4
    #                '---------- +5 ---------> 
    # T(N*amount))    N - num of coins
    # S(amount)
    def change_dp(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(int)
        coins.sort()
        dp[0] = 1        
        for c in coins:
            for a in range(min(coins), amount+1):
                if a-c in dp:
                    dp[a] += dp[a-c]
        if amount in dp:
            return dp[amount]
        else:
            return 0

def test_fixture(solution):
    testdata = [  # (input, expect),
        (([1,2,5], 5), 4),
        (([2], 3), 0),
        (([10], 5), 0),
        (([10], 10), 1),
        # ((),),
    ]

    for i in range(len(testdata)):
        ret = solution.change(testdata[i][0][1],testdata[i][0][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t\t{} expect {}".format(testdata[i][0], ret, 'pass' if ret==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    

