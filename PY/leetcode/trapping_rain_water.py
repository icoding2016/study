"""
42. Trapping Rain Water
Hard
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5


Ideas:
  First find all the peeks.  {x:height_x}   x is the location (index in height)
    peek is where  height(i-1)<height(i)>height(i+1)
  Find the highest, then go left and right side respectively, 
    for each side, while moving from cur highest to side: find the 2nd highest, and calculate the water between highest and 2nd-highest, 
    then move further aside (highest_x = 2nd_hihest_x), scope: left/right side of the peeks from cur highest.
    e.g.
        lh3 <- lh2     <--     h1 -->  rh2 --> rh3  -->   rh4
                                |
                |               |
        |       |       |       |       |       |
        |   |   |   |   |   |   |   |   |   |   |   |   _   |    

    total = water(lh2,lh3, hight_lh3) + water(h1, lh2, hight_lh2) + water(h1,rh2,hight_rh2) + water(rh2,rh3,hight_rh3) + water(h3,rh4,hight_rh4)


"""


from typing import List
from utils.testtools import test_fixture


class Solution:
    def trap(self, height: List[int]) -> int:
        self.height = height
        return self.trap1(height)

    # T(N) ?
    def trap1(self, height: List[int]) -> int:
        # find peeks
        peeks = {}  # {x:height}    peek is where the lpeeks is lower and right is higher.
        last = cur = 0
        for i in range(len(height)):
            cur = height[i]
            if cur >= last:
                if i == len(height)-1:
                    peeks[i] = cur
                elif cur > height[i+1]:
                    peeks[i] = cur
                last = cur
            else:
                last = cur
        
        if len(peeks) <= 1:
            return 0

        total = 0
        # peeks_list = [i for i in peeks]
        h1_at = h2_at = 0
        h1_at = max(peeks, key=lambda x:peeks[x])
        curpeeks = peeks
        while curpeeks:  # cal the left
            lpeeks = {i:curpeeks[i] for i in curpeeks if i < h1_at}   #left side of curpeeks from h1_at
            if not lpeeks:
                break
            h2_at = max(lpeeks, key=lambda x:lpeeks[x])
            total += self.calWater(h2_at, h1_at, peeks[h2_at])
            curpeeks = lpeeks
            h1_at = h2_at
        curpeeks = peeks

        h1_at = max(peeks, key=lambda x:peeks[x])
        curpeeks = peeks
        while curpeeks:
            rpeeks = {i:curpeeks[i] for i in curpeeks if i > h1_at}
            if not rpeeks:
                break
            h2_at = max(rpeeks, key=lambda x:rpeeks[x])
            total += self.calWater(h1_at, h2_at, peeks[h2_at])
            h1_at = h2_at
            curpeeks = rpeeks
        return total

    def calWater(self, lpeeks, right, level) -> int:
        water = 0
        for h in self.height[lpeeks:right+1]:
            water += level - h if level > h else 0
        return water


def test():
    data = [
        (([0,1,0,2,1,0,1,3,2,1,2,1],),6),
        (([4,2,0,3,2,5],),9),
        (([0,1,1,2,3,3,2,1,0,0,],),0),
        (([3,3,3,3,4],),0),
        (([2,2,2,1,2,2,1],),1),
        (([0,1,2,2,3,2,1,0,1,2],),4),
        (([0,1,0,2,1,0,1,3,2,1,2,1, 2, 0, 4,2,3,1,1,3,3,1,4,0,3,2,1,3,2,1,2,4,3,5,1,4,3,5,3,1,1,2,4],),64),
    ]
    s = Solution()
    test_fixture(s.trap, data)


test()
