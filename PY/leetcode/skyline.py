"""
218. The Skyline Problem
Hard
https://leetcode.com/problems/the-skyline-problem/

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. 
Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. 
Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, 
which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. 
Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: 
There must be no consecutive horizontal lines of equal height in the output skyline. 
For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; 
the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

Example 1:
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

Example 2:
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
 

Constraints:
1 <= buildings.length <= 10^4
0 <= lefti < righti <= 2^31 - 1
1 <= heighti <= 2^31 - 1
buildings is sorted by lefti in non-decreasing order.


Solution:
  1. record all max_hight at all x coordinatins -> hights[]
     goes through hights[], mark all (x,y) where the hight changes
     pro: logic easy, 
     con: to big array hights[2^31-1]

  2. make use of the constrain: 'buildings is sorted by left(i) in non-decreasing order.'
     buildings[i], take i as the building id
     record building height in dict heights = {<x_left>:<height>, }
     have a dict tracking all the lefts(open) and rights(close) in ascending order,   points = {x_i:(building_i, 'l'/'r',), }
     keep a dict (open_builds) tracking the 'open' buildings, 
       when reach a 'l' in points, 'open' a new building, when 'r' close a building and remove it from open_builds 
       at the same time, track cur_skyline (max height in open_builds), add point to skyline[] when cur_skyline change

     open_builds = {left_i:[li,ri,hi], left_j:[lj,rj,hj], }
       => open_heights = [open_buildings[x][2] for x in open_buildings]
       => cur_skyline = max(open_heights)


Note:
  - the 'ground' between buildings need to be marked.
  - within the building, mark all the x with height, outside the building, just mark one point (x=right+1) of ground, to save space

"""


from collections import deque
from typing import List
from utils.testtools import test_fixture


# import math
# _MAX_WIDTH = math.pow(2,31)

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        return self.skyline2(buildings)

    # T(B)    B=Building_num
    def skyline2(self, buildings: List[List[int]]) -> List[List[int]]:
        building_info = {}  # {id:[l,r,h]}
        x_axis = deque()  # [(x,[(id,'l'/'r'),..]), ] 

        def queue_insert(x:int, build_idx:int, flag:str):    # O(2B)
            nonlocal x_axis    # [(x, [(build_id1, flag).. (build_idi, flag)]) ]
            index = 0
            # searching from the right side is more efficient
            if not x_axis:
                x_axis.append((x, [(build_idx, flag),]))
                return
            for i in range(len(x_axis)-1, -1, -1):
                if x_axis[i][0] == x:
                    x_axis[i][1].append((build_idx, flag))
                    return
                elif x_axis[i][0] > x:
                    index = i
                    continue
                else:
                    index = i+1
                    break
            x_axis.insert(index, (x,[(build_idx, flag)]))    
    
        for i, (l,r,h) in enumerate(buildings):
            building_info[i] = [l,r,h]  # dict for finding building info by build_idx (left_i)
            queue_insert(l, i, 'l')
            queue_insert(r, i, 'r')

        skyline = []
        open_buildings = deque()    # [building_id(=left_i), ]
        open_heights = []
        pre_x = 0 
        pre_skyline = cur_skyline = 0
        while x_axis:
            x, vl = x_axis.popleft()
            for building_id, flag in vl:
                if flag == 'l':  # open
                    open_buildings.append(building_id)
                else:  # close
                    open_buildings.remove(building_id)
            open_heights = [building_info[id][2] for id in open_buildings]
            cur_skyline = max(open_heights) if open_heights else 0
            if cur_skyline != pre_skyline:
                skyline.append([x, cur_skyline])
            else:
                continue
            pre_x = x
            pre_skyline = cur_skyline
        if pre_skyline != 0:
            skyline.append(pre_x, pre_skyline)
        return skyline


    # use dict + deque (llist).
    # time exceeded
    # T()   B*width*Width
    # S(Width)    Width=from the left of the most left building to the right of the most right side building
    def skyline1(self, buildings: List[List[int]]) -> List[List[int]]:
        # hights = [0 for _ in range(_MAX_WIDTH)]
        heights = self.HeightList()   # [<x,h>,]
        skyline = []
        # maxr = max(buildings, key=lambda x:x[1])
        for l,r,h in buildings:
            for x in range(l, r+1):
                if x in heights:
                    heights[x] = max(heights[x], h)
                else:
                    heights[x] = h      # that wastes memory, any improvement?
            heights[r+1] = heights[r+1] if r+1 in heights else 0    # mark ground
        pre_h = 0
        key = None
        for x in heights:
            h = heights[x]
            if h > pre_h:
                skyline.append([x, h])
                pre_h = h
            elif h < pre_h:
                skyline.append([key, h])
                pre_h = h
            key = x
        if heights[key] != 0:
            skyline.append([key, 0])
        return skyline        

    class HeightList():
        def __init__(self):
            self.dict = dict()
            self.queue = deque()

        def __contains__(self, key) -> bool:
            return key in self.dict

        def __setitem__(self, key, value):
            index = 0
            if not key in self.dict:    # need insert to queue
                for i, k in enumerate(self.queue):
                    if k < key:
                        index = i+1
                        continue
                    else:
                        break
                self.queue.insert(index, key)
            self.dict[key] = value

        def __getitem__(self, key):
            if key in self.dict:
                return self.dict[key]
            raise KeyError(f"{key}")

        def __iter__(self):
            self.index = 0
            return self
        
        def __next__(self):
            if self.index < len(self.queue):
                k = self.queue[self.index]
                self.index += 1
                return k
            raise StopIteration()        




def test():
    data = [
        (([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]],),[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]),
        (([[0,2,3],[2,5,3]],),[[0,3],[5,0]]),
        (([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8], [20,24,9], [26,30,11], [40,50,6], [46,48,8]],),[[2,10],[3,15],[7,12],[12,0],[15,10],[20,9],[24,0],[26,11],[30,0],[40,6],[46,8],[48,6],[50,0]]),
        (([[4,9,10],[4,9,15],[4,9,12],[10,12,10],[10,12,8]],),[[4,15],[9,0],[10,10],[12,0]]),
    ]
    s = Solution()
    test_fixture(s.getSkyline, data)

test()