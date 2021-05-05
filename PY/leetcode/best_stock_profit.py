# Best Time to Buy and Sell Stock
# Easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# 
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
#   and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
# 
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
# 
# 
# 
# Ideas:
#   The question is to find the max gap (right-left) between 2 elements in an array.
#   For each position i,  P[i] = right_max - left_min
# 
# 
# 
# #

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        return self.maxProfit_dp(prices)
        #return self.maxProfit_bf(prices)

    # O(N)     O(N)*4
    def maxProfit_dp(self, prices: List[int]) -> int:
        N = len(prices)
        i = 0
        minmax=[[None, None] for i in range(N)]
        minmax[0] = [prices[0], None]
        minmax[N-1] = [None, prices[N-1]]
        for i in range(1, N):
            minmax[i][0] = min(minmax[i-1][0], prices[i])
        for i in range(N-2,-1,-1):
            minmax[i][1] = max(minmax[i+1][1], prices[i+1])
        maxp = [0]*(N-1)
        for i in range(N-1):
            maxp[i] = minmax[i][1] - minmax[i][0]
        result = max(maxp)
        return result if result > 0 else 0

    def maxProfit_bf(self, prices: List[int]) -> int:
        N = len(prices)
        maxgap = None
        for i in range(N-1):
            for j in range(i+1,N):
                gap = prices[j] - prices[i]
                if maxgap is None:
                    maxgap = gap
                elif gap > maxgap:
                    maxgap = gap
        return maxgap if maxgap > 0 else 0


def test_fixture(s:Solution):
    testdata = [  # (input, expect),
        (([7,1,5,3,6,4],), 5),
        (([1],), 0),
        (([7,6,4,3,1],), 0),
        (([5,5,5],),0),
        (([5,7,3,9,2,8],), 6),
        (([5,5,3,5,2,5,6,4,5],), 4),
    ]
    for i in range(len(testdata)):
        ret = s.maxProfit(*testdata[i][0])
        exp = testdata[i][1]
        #exp = s.maxProfit_bf(*testdata[i][0])
        print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))
import timeit
def test():
    s = Solution()
    test_fixture(s)
test()

        
