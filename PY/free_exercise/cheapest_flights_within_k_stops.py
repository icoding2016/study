"""
787. Cheapest Flights Within K Stops
Medium
https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
If there is no such route, return -1.
 

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.


Constraints:
    1 <= n <= 100
    0 <= flights.length <= (n * (n - 1) / 2)
    flights[i].length == 3
    0 <= fromi, toi < n
    fromi != toi
    1 <= pricei <= 104
    There will not be any multiple flights between two cities.
    0 <= src, dst, k < n
    src != dst

    
Ideas:
  1) Graph DFS
  2) DIJKSTRA


"""
from typing import List
from sys import maxsize
from collections import deque


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = {}
        for s, d, c in flights:
            if s not in graph:
                graph[s] = [(d, c)]
            else:
                graph[s].append((d, c))
        # return self.cheapest_dfs(n, graph, src, dst, k)
        return self.dijkstra_k(
            graph, src, dst, k + 1
        )  # k is the max middle stop#, so max steps = k+1

    def cheapest_dfs(self, n: int, graph: dict, src: int, dst: int, k: int) -> int:
        min_cost = -1
        for cost in self.dfs(graph, src, dst, k):
            if cost >= 0:
                if min_cost == -1:
                    min_cost = cost
                else:
                    min_cost = min(min_cost, cost)
        return min_cost

    # T: O(V+E)
    # S: O(V+E)    O(V+E) for graph_data + O(V) for dfs
    def dfs(self, g, s, d, k, cost=0, path=None):
        if None == path:
            path = [
                s,
            ]
        if s == d:
            yield cost
            return
        if k < 0:
            return
        if s not in g:
            return
        for n, c in g[s]:
            if n not in path:
                for cst in self.dfs(g, n, d, k - 1, cost + c, path + [n]):
                    yield cst

    # The original Dijkstra does not work well for the case with k step limitationn
    # When both shorter path with steps > k and bigger path within k steps exist, it will give the former. (only the shorted steps are recorded)
    #
    #  T: O(k*(e+V))    V:vertices#,  e:max edge# per node,  V in e+V for find min. (can improve to logV with min-heap)
    #    O(V*(e+V)) if without k limitation:
    # S: O(V+E)
    def dijkstra(self, graph: dict, src: int, dst: int, k: int) -> int:
        if src not in graph:
            return -1

        costs = {(src, d): c for d, c in graph[src]}  # track costs of (src, node)
        if (src, dst) not in costs:
            costs[(src, dst)] = maxsize

        processed = [src]
        while costs and k > 0:
            src, cur = min(costs, key=lambda x: costs[x])
            # print(costs, f"{(src, cur)}", k)
            if cur == dst:
                break
            if cur not in graph:
                del costs[(src, cur)]  # the path cannot reach dst, try next
                continue
                # if k <= 1:
                #     continue  # try other options
                # else:
                #     del costs[(src, cur)]  # the path cannot reach dst, try next
                #     continue
            for n, c in graph[cur]:
                if n in processed:
                    continue
                if (src, n) not in costs:
                    costs[(src, n)] = costs[(src, cur)] + c
                else:
                    costs[(src, n)] = min(costs[(src, n)], costs[(src, cur)] + c)
            k -= 1
            processed.append(cur)
            del costs[(src, cur)]

        print(costs)
        return costs[(src, dst)] if costs[(src, dst)] != maxsize else -1

    def dijkstra_k(self, graph: dict, src: int, dst: int, k: int) -> int:
        if src not in graph:
            return -1
        costs = {(d, 1): c for d, c in graph[src]}

        def get_min(cst) -> tuple:
            return min(cst, key=lambda x: cst[x])

        while costs:
            cur, i = get_min(costs)
            # print(costs, f"pick {(cur, i)}")
            if cur == dst:  # and i <= k:
                break  # found the shortest within k steps
            if cur not in graph or i >= k:
                del costs[(cur, i)]
                continue
            for n, c in graph[cur]:
                if (n, i + 1) not in costs:
                    costs[(n, i + 1)] = costs[(cur, i)] + c
                else:
                    costs[(n, i + 1)] = min(costs[(n, i + 1)], costs[(cur, i)] + c)
            del costs[(cur, i)]  # visited

        costs_k = {(d, i): c for (d, i), c in costs.items() if i <= k and d == dst}
        # print(f"costs_k: {costs_k}")
        if not costs_k:
            return -1
        return min(costs_k.values())


test_data = [
    (
        [4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1],
        700,
    ),
    ([3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1], 200),
    ([3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0], 500),
    (
        [
            5,
            [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]],
            2,
            1,
            1,
        ],
        -1,
    ),
    (
        [4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1],
        6,
    ),  # not following the shortest path due to k
    (
        [
            17,
            [
                [0, 12, 28],
                [5, 6, 39],
                [8, 6, 59],
                [13, 15, 7],
                [13, 12, 38],
                [10, 12, 35],
                [15, 3, 23],
                [7, 11, 26],
                [9, 4, 65],
                [10, 2, 38],
                [4, 7, 7],
                [14, 15, 31],
                [2, 12, 44],
                [8, 10, 34],
                [13, 6, 29],
                [5, 14, 89],
                [11, 16, 13],
                [7, 3, 46],
                [10, 15, 19],
                [12, 4, 58],
                [13, 16, 11],
                [16, 4, 76],
                [2, 0, 12],
                [15, 0, 22],
                [16, 12, 13],
                [7, 1, 29],
                [7, 14, 100],
                [16, 1, 14],
                [9, 6, 74],
                [11, 1, 73],
                [2, 11, 60],
                [10, 11, 85],
                [2, 5, 49],
                [3, 4, 17],
                [4, 9, 77],
                [16, 3, 47],
                [15, 6, 78],
                [14, 1, 90],
                [10, 5, 95],
                [1, 11, 30],
                [11, 0, 37],
                [10, 4, 86],
                [0, 8, 57],
                [6, 14, 68],
                [16, 8, 3],
                [13, 0, 65],
                [2, 13, 6],
                [5, 13, 5],
                [8, 11, 31],
                [6, 10, 20],
                [6, 2, 33],
                [9, 1, 3],
                [14, 9, 58],
                [12, 3, 19],
                [11, 2, 74],
                [12, 14, 48],
                [16, 11, 100],
                [3, 12, 38],
                [12, 13, 77],
                [10, 9, 99],
                [15, 13, 98],
                [15, 12, 71],
                [1, 4, 28],
                [7, 0, 83],
                [3, 5, 100],
                [8, 9, 14],
                [15, 11, 57],
                [3, 6, 65],
                [1, 3, 45],
                [14, 7, 74],
                [2, 10, 39],
                [4, 8, 73],
                [13, 5, 77],
                [10, 0, 43],
                [12, 9, 92],
                [8, 2, 26],
                [1, 7, 7],
                [9, 12, 10],
                [13, 11, 64],
                [8, 13, 80],
                [6, 12, 74],
                [9, 7, 35],
                [0, 15, 48],
                [3, 7, 87],
                [16, 9, 42],
                [5, 16, 64],
                [4, 5, 65],
                [15, 14, 70],
                [12, 0, 13],
                [16, 14, 52],
                [3, 10, 80],
                [14, 11, 85],
                [15, 2, 77],
                [4, 11, 19],
                [2, 7, 49],
                [10, 7, 78],
                [14, 6, 84],
                [13, 7, 50],
                [11, 6, 75],
                [5, 10, 46],
                [13, 8, 43],
                [9, 10, 49],
                [7, 12, 64],
                [0, 10, 76],
                [5, 9, 77],
                [8, 3, 28],
                [11, 9, 28],
                [12, 16, 87],
                [12, 6, 24],
                [9, 15, 94],
                [5, 7, 77],
                [4, 10, 18],
                [7, 2, 11],
                [9, 5, 41],
            ],
            13,
            4,
            13,
        ],
        47,
    ),
]


def test():
    solution = Solution()
    for d, ep in test_data:
        ret = solution.findCheapestPrice(*d)
        print(f"{d} -> {ret} (expect {ep}): {'Pass' if ep==ret else 'Fail'}")


test()
