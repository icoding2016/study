# MST (Minimum Spanning Tree)
#   Kruskal's Algorithm
#
# Steps: 
#  1. Sort all the edges in non-decreasing order of their weight. 
#  2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. 
#  3. Repeat step#2 until there are (V-1) edges in the spanning tree.
# 
# 
# 
# 
#  

from collections import defaultdict
from typing import TypeVar
import heapq
from utils.testtools import test_fixture


T = TypeVar('T')


class Vertex(object):
    def __init__(self, id:str) -> None:
        self.id = id
        self.edges = {}  # {vertex_n:weight_n, ...}


class Graph():
    def __init__(self) -> None:
        self.vertices = []  # vertex: ()

    def find(self, id:str) -> Vertex:
        for v in self.vertices:
            if v.id == id:
                return v
        return None

    def add_edge(self, id1:str, id2:str, weight:int, bidirection=False) -> None:
        v1 = self.find(id1)
        if not v1:
            v1 = Vertex(id1)
            self.vertices.append(v1)
        v2 = self.find(id2)
        if not v2:
            v2 = Vertex(id2)
            self.vertices.append(v2)
        v1.edges[v2] = weight
        if bidirection:
            self.add_edge(id2, id1, weight, bidirection=False)

    def __str__(self) -> str:
        s = ''
        for v in self.vertices:
            s += f'[{v.id}]:\n'
            for e, w in v.edges.items():
                s +=f'  {v.id}--({w})-->{e.id}'
            s += '\n'

        return s

    @staticmethod
    def create(data:list[tuple[str,str,int]], bidiretion=False) -> 'Graph':
        g = Graph()
        for v, e, w in data:
            g.add_edge(v, e, w, bidirection=bidiretion)
        return g

    def bfs(self) -> None:
        if not self.vertices:
            return
        q = [self.vertices[0]]
        visited = dict()
        while q:
            v = q.pop(0)
            for e in v.edges:
                if e not in q and e not in visited:
                    q.append(e)
            visited[v] = True
            yield v.id

    def dfs(self) -> None:
        if self.vertices:
            for x in Graph.dfs_r(self.vertices[0]):
                yield x

    @classmethod
    def dfs_r(cls, cur:'Vertex', path:list=None, visited:dict=None) -> None:
        if None == path:
            path = []
        if None == visited:
            visited = {}
        if cur in path:
            return
        for e in cur.edges:
            if e not in path and e not in visited:
                for x in cls.dfs_r(e, path+[cur], visited):
                    yield x
        visited[cur] = True
        yield cur.id

    def check_loop(self, vertex:Vertex) -> bool:
        """Check if the given vertex is in a loop in the graph"""
        return self._check_loop_r(vertex)


    def _check_loop_r(self, vertex:Vertex, path:list=None, visited:dict=None) -> bool:
        if None == path:
            path = []
        if None == visited:
            visited = {}
        if vertex in path:
            return True
        found = False
        for e in vertex.edges:
            if e in path:
                return True
            if e not in visited:
                if self._check_loop_r(e, path+[vertex], visited):
                    return True
        visited[vertex] = True
        return False


class SimpleGraph(object):
    """A simple un-direction graph initialized by dict of {(s,d):weight, ..}"""
    def __init__(self, edges_data: dict) -> None:
        self.edges = edges_data    # {(source, dest):weight, ...}
        self.gen_graph()
    
    def gen_graph(self):
        self.vertices = {}    # {s1:[(d11,w11), (d12,w12), ..], s2:[(d21,w21), (d22, w22), ..], ..}
        for (s, d) , w in self.edges.items():
            if s not in self.vertices:
                self.vertices[s] = [(d, w)]
            else:
                self.vertices[s].append((d, w))
            if d not in self.vertices:
                self.vertices[d] = [(s, w)]
            else:
                self.vertices[d].append((s, w))

    def __str__(self) -> str:
        s = ''
        s += f'edges: {self.edges}\n'
        for v, edges in self.vertices.items():
            s += f'{v}: {edges}\n' 
        return s

    def check_loop(self, v:str=None) -> bool:
        if v:
            return self._check_loop_r(v)
        else:
            for v in self.vertices:
                if self._check_loop_r(v):
                    return True
            return False

    def _check_loop_r(self, v:str, path:list=None, visited:dict=None) -> bool:
        if path == None:
            path = []
        if visited == None:
            visited = dict()
        # if v in path and v not in visited:
        #     return True
        for e, _ in self.vertices[v]:
            if e in path and path[-1] != e and e not in visited:    # Note: for undirectional graph, every 'edge' has 2 a->b, b->a,
                                                                    # so v-e-v should be ommitted in loop-check
                # print(f'v->e {v},{e} found loop path: {path}')
                return True
            if e not in path and e not in visited:
                if self._check_loop_r(e, path+[v], visited):
                    return True
        visited[v] = True
        return False

def Kruska(edges:dict) -> tuple[list[tuple[str,str]], int]:
    """Minimum Spanning Tree Kruska Algorithm
    Args:
      a dict of edges, in form of {(s,d):w, ...}
    Returns:
      (list-of-edges, total cost), the edges are represented by (id1,id2)
    """

    minq = sorted(edges, key=lambda x:edges[x])
    cost = 0
    selected = {}
    for edge in minq:
        selected[edge]=edges[edge]
        sg = SimpleGraph(selected)
        if sg.check_loop(edge[0]) or sg.check_loop(edge[1]):
            del selected[edge]
            #print(f'skip edge {edge}')
            continue 
        cost += edges[edge]
        #print(f'add edge {edge}')
    return ([pair for pair in selected], cost)


def test_kruskal():
    sg_data1 = {
        ('a', 'b'):3, ('a', 'c'):4, ('a', 'd'):5,  ('a', 'f'):1,
        ('b', 'c'):3, ('b', 'd'):8, ('c', 'd'):6,
        ('b', 'e'):4, ('d', 'e'):3, ('f', 'c'):7
    }
    test_data = [
        ((sg_data1,), ([('a', 'f'), ('a', 'b'), ('b', 'c'), ('d', 'e'), ('b', 'e')], 14)),
    ]
    def cmpr(r, e):
        if r[1] != e[1]:
            return False
        if len(r[0]) != len(e[0]):
            return False
        num_match=0
        for a,b in r[0]:
            if (a,b) in e[0] or (b,a) in e[0]:
                num_match += 1
        return num_match == len(r[0])
    print('test krustal')
    test_fixture(Kruska, test_data, comp=cmpr)

def test():
    # data for undirectional graph
    data = [
        ('a', 'b', 3), ('a', 'c', 4), ('a', 'd', 5),  ('a', 'f', 1),
        ('b', 'c', 3), ('b', 'd', 8), ('c', 'd', 6),
        ('b', 'e', 4), ('d', 'e', 3), ('f', 'c', 7)
    ]
    g = Graph.create(data, bidiretion=True)
    print(g)

    print('SimpleGraph')
    sg_data = {
        ('a', 'b'):3, ('a', 'c'):4, ('a', 'd'):5,  ('a', 'f'):1,
        ('b', 'c'):3, ('b', 'd'):8, ('c', 'd'):6,
        ('b', 'e'):4, ('d', 'e'):3, ('f', 'c'):7
    }
    sg = SimpleGraph(sg_data)
    print(sg)
    
    test_kruskal()
    

test()    
