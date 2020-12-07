# Network Delay Time
# Medium
# There are N network nodes, labelled 1 to N.
# Given times, a list of travel times as directed edges times[i] = (u, v, w), 
# where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
# Now, we send a signal from a certain node K. 
# How long will it take for all nodes to receive the signal? If it is impossible, return -1.
#
# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2
#
# Note:
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
# 
# 
# Ideas:
#   1. Graph travesal
#     Notes: 
#     1) Reachability: there may be nodes that is not reachable, so get the num of all 'dst' nodes from graph and compare N. 
#        if num(dst & starting node) == N then all reachable
#     2) This is a 'shortest path to all nodes' question, find the shortest path for each node, 
#        then the max time cost of all the nodes is the time that it takes for the signal to reach every nodes.
#     3) It is not BFS or DFS.
#        (a) The signal to all the neighbors start at the same time, so don't add the time-cost all toghter as the DFS path cost does.
#        (b) Need to try all paths, not simply traversal all nodes, so 'visited' is not used (a node should be visited from different routings)
#  2. Short-time path algorithm (e.g. dijkstra)
#      
# # 

from typing import List
from collections import defaultdict
from heapq import heappush, heappop, heapify
import sys

# T(V*V)
class Solution(object):
    INFINITY = sys.maxsize

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        if not times:
            return 0
        nodes = defaultdict(list)  # {src:[(dst, delay), ...]}
        allnodes = []
        for s,d,t in times:
            if s in nodes:
                if d not in nodes[s]:
                    nodes[s].append((d, t))
            else:
                nodes[s] = [(d, t)]
            if s not in allnodes:
                allnodes.append(s)
            if d not in allnodes:
                allnodes.append(d)
        if K not in allnodes:
            allnodes.append(K)
        if len(allnodes) < N:
            return -1

        delays = defaultdict(int)      # {dst:min-delay}
        for n in allnodes:
            delays[n] = self.INFINITY
        delays[K] = 0

        while allnodes:                                         # O(V)
            src, sc = self.get_lowest_cost(delays, allnodes)    # O(V)
            for dst, c in nodes[src]:                           # O(Vsrc) (Vsrc <= V)
                delay = c + sc
                if delay < delays[dst]:
                    delays[dst] = delay
            allnodes.remove(src)
        max_delay = max([delays[d] for d in delays])
        return max_delay if max_delay != self.INFINITY else -1

    def get_lowest_cost(self, delays:dict, allnodes:list) -> (int, int):
        min_delay = self.INFINITY
        if not allnodes:
            return None, min_delay
        min_node = allnodes[0]
        for node in allnodes:
            if delays[node] < min_delay:
                min_delay = delays[node]
                min_node = node
        return min_node, min_delay


class Solution2(object):
    INFINITY = sys.maxsize

    # the implementation has issue. 
    #   if no 'end' (find shortest path for all nodes)
    #   heappush(to_relax, [delays[dst], dst]) may cause infinit loop, need an exist condition 
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        if not times:
            return 0
        nodes = defaultdict(list)  # {src:[(dst, delay), ...]}
        for t in times:
            if t[0] in nodes:
                if t[1] not in nodes[t[0]]:
                    nodes[t[0]].append((t[1], t[2]))
            else:
                nodes[t[0]] = [(t[1], t[2])]

        delays = defaultdict(int)      # {dst:min-delay}
        allnodes = []
        for n, dl in nodes.items():
            if n not in allnodes:
                allnodes.append(n)
            for d, c in dl:
                if d not in allnodes:
                    allnodes.append(d)
        for n in allnodes:
            delays[n] = self.INFINITY
        delays[K] = 0
        to_relax = [[0, K]]    # starting node

        while to_relax:
            sc, src = heappop(to_relax)
            for dst, c in nodes[src]:
                delay = c + sc
                if delay < delays[dst]:
                    delays[dst] = delay
                exist = False
                for i in range(len(to_relax)):
                    if dst == to_relax[i][1]:
                        to_relax[i][0] = delays[dst]
                        heapify(to_relax)
                        exist = True
                        break
                if not exist:
                    heappush(to_relax, [delays[dst], dst])
        max_delay = max([delays[d] for d in delays])
        return max_delay if max_delay != self.INFINITY else -1


class Solution1(object):
    INFINITY = sys.maxsize
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        if not times:
            return 0
        nodes = defaultdict(list)  # {src:[(dst, delay), ...]}
        dst = []
        for t in times:
            if t[0] in nodes:
                if t[1] not in nodes[t[0]]:
                    nodes[t[0]].append((t[1], t[2]))
            else:
                nodes[t[0]] = [(t[1], t[2])]
            if t[1] not in dst:
                dst.append(t[1])
        reachable = len(dst)
        reachable += 1 if K not in dst else 0
        if reachable < N:
            return -1

        stimes = self.shortest_time(nodes, K)
        return max([stimes[n] for n in stimes])

    def shortest_time(self, nodes:dict, cur_node:int, path:list=None,short_times:dict=None)->dict:
        if path == None:
            path = []
        if short_times == None:
            short_times = dict()  # {dst:time}
            short_times[cur_node] = 0
        
        t = 0
        if cur_node in path:
            return short_times
        path.append(cur_node)
        for dst, delay in nodes[cur_node]:
            t = short_times[cur_node] + delay
            if dst in short_times:
                short_times[dst] = min(short_times[dst], t)
            else:
                short_times[dst] = t
            if dst not in path:
                _ = self.shortest_time(nodes, dst, path, short_times)
        path.pop()
        return short_times


        


def test_fixture(solution):
    testdata = [  # (input, expect),
        (([[1,2,1],[2,3,7],[1,3,4],[2,1,2]],4,1), -1),
        (([[2,1,1],[2,3,1],[3,4,1]], 4, 2), 2),
        (([[1,2,1]], 2, 1), 1),
        (([[1,2,1], [1,3,2]], 3, 1), 2),
        (([[1,2,1], [1,3,2]], 3, 2), -1),
        (([[1,2,2],[1,4,4],[2,4,1],[4,3,2],[4,5,2]], 5, 1), 5),
        (([[1,2,2],[1,4,4],[2,4,1],[4,3,2],[4,5,2]], 5, 2), -1),
        (([[1,2,1],[2,3,2],[1,3,2]], 3, 1), 2),
        (([[1,4,4],[1,2,1],[1,3,2],[2,3,2],[2,5,3],[3,4,1]], 5, 1), 4),
        (([[1,4,4],[1,2,1],[1,3,2],[2,3,2],[2,5,3],[3,4,1]], 5, 2), -1),
        (([[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]],5,5),31),
        (([[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]],5,3),59)
    ]

    for i in range(len(testdata)):
        ret = solution.networkDelayTime(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t\t{}, expect {}".format(testdata[i][0], ret, 'pass' if ret==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    
