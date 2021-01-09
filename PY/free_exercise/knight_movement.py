# Given the chess board size N, coordination:(0,N-1)
# knight starting position kstart(kx1,ky1), end position kend(kx2,ky2), and bishop position(bx1,bx2), 
# find the minimum number of moves for the knight to move from its starting position to the end position. 
# The knight cannot move on any square that the bishop is attacking, but it can go on those squares if the knight captures the bishop.
# 
# Note:
#  - knight can move to 'L' position in any direction.  (x+/-1, y+/-2) or (x+/-2, y+/-1)
#    the Knight may jump over pieces.  
#  - bishop can move diagonally, 
#    A bishop captures by occupying the square on which an enemy piece sits
#
# 
# Solution:
#   Dijkstra + validating move-destination
# 
# #


from sys import maxsize
#from collections import deque


class Solution(object):
    # def __init__(self, N:int, kend:tuple, b:tuple):
    #     self.b = b
    #     self.N = N
    #     self.kend = kend

    def minKightMoves(self, N:int, kstart:tuple, kend:tuple, b:tuple)->int:
        #return self.minKightMoves_recursive(N, kstart, kend, b)
        return self.dijkstra(N, kstart, kend, b)

    # T(S*8)   S:size-of-board (N*N)
    def dijkstra(self, N:int, k:tuple, kend:tuple, b:tuple, costs:dict=None)->int:
        if costs == None:
            #costs = [[maxsize for i in range(N)] for j in range(N)]
            costs = {k:0}  # {(x,y):cost, ...}, cost of p is Infinity is p not in costs

        todo = []
        todo.append(k)
        done = []
        while todo:
            cur, cur_cost = self.find_min_cost(todo, costs)
            if cur == kend:
                return cur_cost
            x = cur[0]
            y = cur[1]
            for jumpto in [(x-1,y-2), (x+1,y-2), (x-1,y+2), (x+1,y+2), (x-2,y-1), (x+2,y-1), (x-2,y+1), (x+2,y+1),]:
                if jumpto in done:
                    continue
                if self.valid_k_landing(N, jumpto, b):
                    if jumpto in costs:
                        costs[jumpto] = min(cur_cost+1, costs[jumpto])
                    else:
                        costs[jumpto] = cur_cost + 1
                    if jumpto not in todo:
                        todo.append(jumpto)
            done.append(cur)
            todo.remove(cur)
        return -1

    def find_min_cost(self, todo:list, costs:dict)->tuple:
        mc = None
        mp = None
        for p in todo:
            if p in costs:
                c = costs[p]
            if not mc:
                mc = c
                mp = p
            elif c < mc:
                mc = c
                mp = p
        return mp, mc

    def minKightMoves_recursive(self, N:int, kstart:tuple, kend:tuple, b:tuple)->int:
        # validate coordinations  # if k[0] >= N or k[1] >=N or ...
        # self.validateCoord()
        steps = [s for s in self.move(N, kstart, kend, b)]
        print('steps: ', steps)
        return min(steps) if steps else -1

    def valid_k_landing(self, N, kto:tuple, b:tuple)->bool:
        if kto[0] >= N or kto[0] < 0 or kto[1] >= N or kto[1] < 0:
            return False 
        if kto == b:
            return True
        if abs(kto[0]-b[0]) == abs(kto[1]-b[1]):
            return False
        return True

    # wrong, does not iterate all the possible paths
    def move(self, N:int, k:tuple, kend:tuple, b:tuple, steps:int=0, path:list=None, visited:set=None)->None:
        if None == path:
            path = [k]
        if None == visited:
            visited = set()
        
        if k == kend:
            #print(steps, path)
            yield steps
            return

        # try 8 L moves
        x = k[0]
        y = k[1]
        for kto in [(x-1,y-2), (x+1,y-2), (x-1,y+2), (x+1,y+2), 
                    (x-2,y-1), (x+2,y-1), (x-2,y+1), (x+2,y+1),]:
            if kto not in path and kto not in visited and self.valid_k_landing(N, kto, b):
                for i in self.move(N, kto, kend, b, steps+1, path+[kto], visited):
                    yield i        
        visited.add(k)
        # for p in [(x-1,y-2), (x+1,y-2), (x-1,y+2), (x+1,y+2), 
        #             (x-2,y-1), (x+2,y-1), (x-2,y+1), (x+2,y+1),]:
        #     if p in visited:
        #         visited.remove(p)



def test_fixture(solution):
    testdata = [  # (input, expect),
        # N,ks,ke,b,
        ((10,(1,2),(5,3),(2,5), ), 3),
        ((10,(1,2),(5,3),(4,5), ), 3),
        ((10,(1,2),(5,3),(4,2), ), -1),     # K2 is in the catchment of bishop
        ((10,(1,2),(4,3),(4,2), ), 4),
        ((10,(1,2),(4,3),(7,2), ), 2),
    ]

    for i in range(len(testdata)):
        ret = solution.minKightMoves(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format(testdata[i][0], ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))



def test():
    s = Solution()
    test_fixture(s)


test()    
