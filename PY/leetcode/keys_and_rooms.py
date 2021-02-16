# Keys and Rooms
# Medium
# https://leetcode.com/problems/keys-and-rooms/

# There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, 
# and each room may have some keys to access the next room. 
# Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  
# A key rooms[i][j] = v opens the room with number v.

# Initially, all the rooms start locked (except for room 0). 
# You can walk back and forth between rooms freely.
# Return true if and only if you can enter every room.

# Example 1:
# Input: [[1],[2],[3],[]]
# Output: true
# Explanation:  
# We start in room 0, and pick up key 1.
# We then go to room 1, and pick up key 2.
# We then go to room 2, and pick up key 3.
# We then go to room 3.  Since we were able to go to every room, we return true.

# Example 2:
# Input: [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can't enter the room with number 2.

# Note:
# 1 <= rooms.length <= 1000
# 0 <= rooms[i].length <= 1000
# The number of keys in all rooms combined is at most 3000.


from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms) <= 1:
            return True
        return self.canVisitAllRooms_1(rooms)
    
    def canVisitAllRooms_1(self, rooms: List[List[int]]) -> bool:
        return self.travel(0, rooms)

    # T(E+V)
    def travel(self, cur:int, rooms:List[List[int]], unlocked:dict=None, visited:dict=None, path:list=None) -> bool:
        if None == path:
            path = []
        if None == visited:
            visited = {}
        if None == unlocked:
            unlocked = {}
        if cur >= len(rooms):
            assert("Invalid room No. %i" % cur)
            return

        unlocked[cur] = True
        if len(unlocked) == len(rooms):
            return True

        path.append(cur)
        for i in rooms[cur]:
            if i not in visited and i not in path:
                self.travel(i, rooms, unlocked, visited, path)
            visited[i] = True
        return len(unlocked) == len(rooms)




def test_fixture(s):
    testdata = [  # (input, expect),
        (([[1],[2],[3],[]],),  True),
        (([[1,3],[3,0,1],[2],[0]],),  False),
        (([[]],),  True),
        (([[1],[2,4],[3],[],[3,5],[2,1,0,7],[],[]], ), False),
        (([[1],[2,4],[3],[6],[3,5],[2,1,0,7],[],[]], ), True),
    ]

    for i in range(len(testdata)):
        ret = s.canVisitAllRooms(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format(testdata[i][0], ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))


import timeit
def test():
    s = Solution()
    test_fixture(s)

test()

