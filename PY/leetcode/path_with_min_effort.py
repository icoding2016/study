# Path With Minimum Effort
# Medium
# https://leetcode.com/problems/path-with-minimum-effort/
#
# You are a hiker preparing for an upcoming hike. 
# You are given heights, a 2D array of size rows x columns, 
# where heights[row][col] represents the height of cell (row, col). 
# You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, 
# (rows-1, columns-1) (i.e., 0-indexed). 
# You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
#
# 
# Example 1:
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
#     1  2  2
#     3  8  2
#     5  3  5
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

# Example 2:
#     1  2  3
#     3  8  4
#     5  3  5
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

# Example 3:
# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
#      1  2  1  1  1
#      1  2  1  2  1
#      1  2  1  2  1
#      1  2  1  2  1
#      1  1  1  2  1
# Output: 0
# Explanation: This route does not require any effort.
 
# Constraints:
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 106



from typing import List
import sys
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.COLS = len(heights[0])
        self.ROWS = len(heights)
        self.heights = heights
        self.min_effort = sys.maxsize
        self.min_path = []
        #return self.minimumEffortPath_dfs((0,0))
        return self.minimumEffortPath_djikstra()

    # T(4^N)    N=number of elements(rowsxcols)
    # S(N)
    # Time limit exceeded.
    def minimumEffortPath_dfs(self, cur:tuple[int], effort:int=0, path:list=None) -> int:
        if None == path:
            path = [(0,0)]

        if cur == (self.COLS-1, self.ROWS-1):
            if effort < self.min_effort:
                self.min_effort = effort
                self.min_path = path.copy()
                return effort
            return self.min_effort
        
        x, y = cur
        neighbors = []
        if x - 1 >= 0:
            neighbors.append((x-1,y))
        if x + 1 < self.COLS:
            neighbors.append((x+1,y))
        if y - 1 >= 0:
            neighbors.append((x, y-1))
        if y + 1 < self.ROWS:
            neighbors.append((x, y+1))
        m = self.min_effort
        for x2,y2 in neighbors:
            if (x2,y2) not in path:  # and (x2,y2) not in visited:
                m = self.minimumEffortPath_dfs((x2,y2), max(effort,abs(self.heights[y2][x2]-self.heights[y][x])), path+[(x2,y2)])
        #visited[(x2,y2)] = True
        return m

    # That implementation 'accumulated effort' (adding the height difference for each step), which is a misunderstanding of the question.
    def minimumEffortPath_dfs_acc(self, cur:tuple[int], effort:int=0, path:list=None, visited:dict=None) -> int:
        if None == path:
            path = []
        if None == visited:
            visited = dict()   # {(x,y):True,...}

        if cur == (self.COLS-1, self.ROWS-1):
            if effort < self.min_effort:
                self.min_effort = effort
                self.min_path = [(0,0)] + path.copy()
                return effort
            return self.min_effort
        
        x, y = cur
        neighbors = []
        if x - 1 >= 0:
            neighbors.append((x-1,y))
        if x + 1 < self.COLS:
            neighbors.append((x+1,y))
        if y - 1 >= 0:
            neighbors.append((x, y-1))
        if y + 1 < self.ROWS:
            neighbors.append((x, y+1))
        m = self.min_effort
        for x2,y2 in neighbors:
            if (x2,y2) not in path:  # and (x2,y2) not in visited:
                m = self.minimumEffortPath_dfs((x2,y2), effort+abs(self.heights[y2][x2]-self.heights[y][x]), path+[(x2,y2)], visited)
        visited[(x2,y2)] = True
        return m


    def minimumEffortPath_djikstra(self) -> int:
        effort = dict()
        for y in range(self.ROWS):
            for x in range(self.COLS):
                effort[(x,y)] = 0 if (x,y)==(0,0) else None
        todo = [n for n in effort]
        while todo:
            x,y = self._get_smallest_effort(todo, effort)
            # update neighbor's 'max effort'
            self.min_path.append((x,y))
            if x-1>=0:
                gap = max(effort[(x,y)], self._effort((x,y), (x-1,y)))
                effort[(x-1,y)] = gap if effort[(x-1,y)]==None else min(effort[(x-1,y)], gap)
            if x+1<self.COLS:
                gap = max(effort[(x,y)], self._effort((x,y), (x+1,y)))
                effort[(x+1,y)] = gap if effort[(x+1,y)]==None else min(effort[(x+1,y)], gap)
            if y-1>=0:
                gap = max(effort[(x,y)], self._effort((x,y), (x,y-1)))
                effort[(x,y-1)] = gap if effort[(x,y-1)]==None else min(effort[(x,y-1)], gap)
            if y+1<self.ROWS:
                gap = max(effort[(x,y)], self._effort((x,y), (x,y+1)))
                effort[(x,y+1)] = gap if effort[(x,y+1)]==None else min(effort[(x,y+1)], gap)
            todo.remove((x,y))
        return effort[(self.COLS-1, self.ROWS-1)]


    # O(V^2E)    4V*V      V (todo loop) 
    #                    * V (_get_smallest_effort is O(V) for now, can be reduced to logV if using heap)
    #                    * E=4 (for neighbors of 1 vertex in worst case)
    # Time limit exceeded.
    # For normal djikstra, O(VElogV) if using heap, or O(V^2E)
    def minimumEffortPath_djikstra_noheap(self) -> int:
        effort = dict()
        for y in range(self.ROWS):
            for x in range(self.COLS):
                effort[(x,y)] = 0 if (x,y)==(0,0) else None
        todo = [n for n in effort]
        while todo:
            x,y = self._get_smallest_effort(todo, effort)
            # update neighbor's 'max effort'
            self.min_path.append((x,y))
            if x-1>=0:
                gap = max(effort[(x,y)], self._effort((x,y), (x-1,y)))
                effort[(x-1,y)] = gap if effort[(x-1,y)]==None else min(effort[(x-1,y)], gap)
            if x+1<self.COLS:
                gap = max(effort[(x,y)], self._effort((x,y), (x+1,y)))
                effort[(x+1,y)] = gap if effort[(x+1,y)]==None else min(effort[(x+1,y)], gap)
            if y-1>=0:
                gap = max(effort[(x,y)], self._effort((x,y), (x,y-1)))
                effort[(x,y-1)] = gap if effort[(x,y-1)]==None else min(effort[(x,y-1)], gap)
            if y+1<self.ROWS:
                gap = max(effort[(x,y)], self._effort((x,y), (x,y+1)))
                effort[(x,y+1)] = gap if effort[(x,y+1)]==None else min(effort[(x,y+1)], gap)
            todo.remove((x,y))
        return effort[(self.COLS-1, self.ROWS-1)]

    def _effort(self, a, b) -> int:
        return abs(self.heights[a[1]][a[0]]-self.heights[b[1]][b[0]])

    def _get_smallest_effort(self, todo, effort) -> tuple[int]:
        assert todo, 'the todo list shouldnt be empty'
        smallest = effort[todo[0]]
        node = todo[0]
        for x,y in todo:
            if effort[(x,y)] == None:
                continue
            elif effort[(x,y)] < smallest:
                smallest = effort[(x,y)]
                node = (x,y)
        return node




def test_fixture(s:Solution):
    testdata = [  # (input, expect),
        (([[1,2,2],[3,8,2],[5,3,5]],), 2),
        (([[1,2,3],[3,8,4],[5,3,5]],), 1),
        (([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],), 0),
        (([[1]],),0),
        (([[1,2,2,4,3],[3,2,3,8,2],[5,4,1,3,5],[4,6,2,3,4],[3,1,1,4,5]],),2),
        (([[1,10,6,7,9,10,4,9]],),9),
        (([[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]],),5)
    ]
    for i in range(len(testdata)):
        ret = s.minimumEffortPath(*testdata[i][0])
        exp = testdata[i][1]
        #exp = s.maxProfit_bf(*testdata[i][0])
        print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))
        # print(s.min_path)
import timeit
def test():
    s = Solution()
    test_fixture(s)
test()











