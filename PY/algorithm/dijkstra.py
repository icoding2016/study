# Giving a graph expressed as [ [src1, dst1, cost1], ... ] and starting point S, 
# find the shortest path to destination D.
# Or another question, to find the shortest path to all other nodes.
# 
# To make it simple, the nodes are represented by number;
# Suppose the cost is in [0, 1000] 
# 
# 
# Dijkstra:
#   - initialize the cost for each node C(node)=infinity
#   - Do 'Relaxation' from starting node. 
#     pick the 'smallest cost' node (from the full set of nodes). If a node is visited, then remove it from the nodes set to visit.
#   - Relaxition: for a node (v, e)  the cost C(e)=min(C(e), C(v)+C(v,e))
#   - 
# 
# # 

import sys
from collections import defaultdict
from heapq import heappush, heappop, heapify

class Solution:
    INFINITY = sys.maxsize

    # T(V*Em*logV)
    def dijkstra(self, graph_data:list, start:int, end:int=None) -> (int,list):
        '''Find the shortest path & cost from A to B
          graph_data:  [[src,dst,cost], ...]
        '''
        graph = defaultdict(list)    # graph with all nodes   {s:[(d,c), (d,c)..]}
        for s,d,c in graph_data:
            graph[s].append((d,c))
            if d not in graph:
                graph[d] = []
        
        C = {n:self.INFINITY for n in graph} 
        C[start] = 0
        path = []
        pq = []
        for s, dl in graph.items():
            for d, t in dl:
                if d == start:
                    heappush(pq, [0, start])
                    continue
                if d not in pq:
                    heappush(pq, [self.INFINITY, d])
        if [0, start] not in pq:
            heappush(pq, [0, start])
        
        prev = None
        while pq:                                      # O(V)
            c, s = heappop(pq)
            for d, c in graph[s]:                      # O(Em) - max edge on single V
                if C[s]+c < C[d]:
                    C[d] = C[s]+c
                    self.update_cost(pq, d, C[d])            # O(VlogV)
            if prev == None:
                prev = s
            else:
                if prev != s:
                    path.append(prev)
                prev = s
            if s == end:
                break        
        if path and path[-1] != end:
            path.append(end)
        print(path)
        return C[end] if C[end]<self.INFINITY else -1, path

    def update_cost(self, costs:list, node:int, cost:int)->None:
        found = False
        for i in range(len(costs)):
            if costs[i][1] == node:
                costs[i][0] == cost
                found = True
                break
        if not found:
            costs.append([cost, node])
        heapify(costs)



    def dijkstra2(self, graph_data:list, start:int, end:int) -> (int,list):
        '''Find the shortest path & cost from A to B
          graph_data:  [[src,dst,cost], ...]
        '''
        graph = defaultdict(list)    # graph with all nodes   {s:[(d,c), (d,c)..]}
        for s,d,c in graph_data:
            graph[s].append((d,c))
            if d not in graph:
                graph[d] = []
        
        C = {n:self.INFINITY for n in graph} 
        C[start] = 0
        path = []
        pq = [(0, start)]
        prev = None
        while pq:                                      # O(V)
            c, s = heappop(pq)
            for d, c in graph[s]:                      # O(Em) - max edge on single V
                if C[s]+c < C[d]:
                    C[d] = C[s]+c
                    heappush(pq, (C[d], d))            # O(logV)
            if prev == None:
                prev = s
            else:
                if prev != s:
                    path.append(prev)
                prev = s
            if s == end:
                break        
        if path and path[-1] != end:
            path.append(end)
        print(path)
        return C[end] if C[end]<self.INFINITY else -1, path




def test_fixture(solution):
    testdata = [  # (input, expect),
        (([[2,1,1],[2,3,1],[3,4,1],[5,6,3]], 2, 4), 2),
        (([[2,1,1],[2,3,1],[3,4,1],[5,6,3]], 4, 5), -1),
        (([[1,2,1]], 1, 2), 1),
        (([[1,2,1], [1,3,2]], 1, 3), 2),
        (([[1,2,1], [1,3,2]], 3, 2), -1),
        (([[1,2,2],[1,4,4],[2,4,1],[4,3,2],[4,5,2]], 1,5), 5),
        (([[1,2,2],[1,4,4],[2,4,1],[4,3,2],[4,5,2]], 3,4), -1),
        # (([[1,2,1],[2,3,2],[1,3,2]], 3, 1), 2),
        # (([[1,4,4],[1,2,1],[1,3,2],[2,3,2],[2,5,3],[3,4,1]], 5, 1), 4),
        # (([[1,4,4],[1,2,1],[1,3,2],[2,3,2],[2,5,3],[3,4,1]], 5, 2), -1),
        # (([[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]],5,5),31),
        # (([[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]],5,3),59)
    ]

    for i in range(len(testdata)):
        ret = solution.dijkstra(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t\t{}, expect {}".format(testdata[i][0], ret[0], 'pass' if ret[0]==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    
