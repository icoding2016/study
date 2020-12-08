#  Coin Change
# Medium
# https://leetcode.com/problems/coin-change/
# You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
#
# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#  
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
# 
# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
# 
# Example 4:
# Input: coins = [1], amount = 1
# Output: 1
# 
# Example 5:
# Input: coins = [1], amount = 2
# Output: 2
# 
# Constraints:
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
# 
# 
# Ideas:
#   For amount N, use coins by value (big to small). The max num of Coin1 is int(amount/coin1). choose coin1 from range(amount/coin1,-1,-1)
#   Note: Choosing the max is not alwasy working,   e.g..  ([5,6,2], 10)    is not 3(6,2,2) but 2(5,5)
#  Solution: recursive: that's brutal force
#
#  Solution: maths:     N - min num of coins to make up amount
#     N(amount) = min(N(amount-coin)+1 for coin in coins)
#     
# # 


from collections import defaultdict
from typing import List
import sys


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # coins.sort(reverse=True)
        # num = self.fewestCoins(coins, amount)
        # return num if num else -1
        return self.fewestCoins_dp(coins, amount)

    # T(amount^N/coin1*coin2*...coinN)   N = num of coins
    def fewestCoins(self, coins: List[int], amount: int, num: int=0) -> int:
        if amount == 0:
            return num
        if not coins and amount > 0:
            return -1
        if amount < 0:
            return -1
        c = coins[0]
        mincoins = sys.maxsize
        for i in range(amount//c, -1, -1):
            n = self.fewestCoins(coins[1:], amount-c*i, num+i)
            if n > 0:
                if n < mincoins:
                    mincoins = n
        return mincoins if mincoins > 0 else -1


    # T(amount*len(coins))
    # S(amount)
    def fewestCoins_dp(self, coins:List[int], amount: int) -> int:
        dp = defaultdict(int)
        for c in coins:
            dp[c] = 1
        am = min(coins)
        while am <= amount:
            for c in coins:
                if am in dp:
                    dp[am+c]=min(dp[am]+1, dp[am+c]) if am+c in dp else dp[am]+1
            am += 1
        if amount in dp:
            return dp[amount]
        return -1


def test_fixture(solution):
    testdata = [  # (input, expect),
        (([1,2,5], 11), 3),
        (([2], 3), -1),
        (([1], 0), 0),
        (([2,5,10], 17),3),
        (([2,5,10], 18),5),
        (([2,5,10], 8), 4),
        (([2,5,10], 3), -1),
        (([186,419,83,408],6249), 20),
        # ((),),
    ]

    for i in range(len(testdata)):
        ret = solution.coinChange(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t\t{} expect {}".format(testdata[i][0], ret, 'pass' if ret==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    

