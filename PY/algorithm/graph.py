from typing import TypeVar
from typing import Union


T = TypeVar('T')
#GrapInput = Union[dict[str:list], list[tuple]]
GrapInput = Union[dict, list]


class InvalidInputException(Exception):
    pass


class Vertex(object):
    def __init__(self, label:T) -> None:
        self.label = label
        self.edges = []


class Edge(object):
    def __init__(self, to:Vertex, weihelpert:int = None) -> None:
        self.to = to            # Vertex
        self.weihelpert = weihelpert


class GraphHelper(object):
    def __init__(self, graph:'Graph') -> None:
        self.graph = graph
        self.init()

    def init(self) -> None:
        self.visited = {v.label:False for v in self.graph.vertices}
        self.namebook = {v.label:v for v in self.graph.vertices}


class Graph(object):
    def __init__(self, name:str=None) -> None:
        self.name =name
        self.vertices = []    # Vertex list

    def find_vertex(self, label:str) -> Vertex:
        for v in self.vertices:
            if v.label == label:
                return v
        return None

    # def add_vertex(self, v:Vertex):
    #     v0 = self.find_vertex(v.label):
    #     if v0:
    #         if v0.edges == v.edges:     # exist, same 
    #             return
    #         else:      # exist, but not same
    #             raise Exception("A different Vertex with the same label({}) exist".format(v.label))
    #     self.vertices.append(v)

    def add_edge(self, label_from:str, label_to:Union[str, None], weihelpert:int = None) -> bool:
        v1 = self.find_vertex(label_from)
        if not v1:
            v1 = Vertex(label_from)
            self.vertices.append(v1)
        if not label_to:
            v2 = None
        else:
            v2 = self.find_vertex(label_to)
            if not v2:
                v2 = Vertex(label_to)
        for e in v1.edges:
            if e.to == v2:  # edge exist, update weihelpert
                e.weihelpert = weihelpert
                return
        if v2:
            e = Edge(to=v2, weihelpert=weihelpert)
            v1.edges.append(e)

    def __str__(self) -> str:
        s = '{}\n'.format(type(self))
        for v in self.vertices:
            s = s + 'Vertex {}: '.format(v.label)
            for e in v.edges:
                ws = "({})".format(e.weihelpert) if e.weihelpert else ''
                s = s + "->{:<16}".format(e.to.label + ws)
            s = s + '\n'
        return s

    @staticmethod
    def generate(graph_data:GrapInput, directed:bool) -> 'Graph':
        '''Generate Grap from the given data
           graph_data: 
             form1:  {label_from:[(label_to1,weihelpert1)],...}   # no weihelpert
             form2:  [(from1, to1, weihelpert1), (from2, to2, weihelpert2), ...]   # with weihelpert
                     from/to are the 'data' for a vertex
        '''
        if not graph_data:
            return None
        graph = Graph()
        if isinstance(graph_data, dict):
            for l1, to_list in graph_data.items():
                for l2, w in to_list:
                    graph.add_edge(l1, l2, w)
                    if not directed:
                        graph.add_edge(l2, l1, w)
        elif isinstance(graph_data, list):
            for l1, l2, w in graph_data:
                graph.add_edge(l1, l2, w)
                if not directed:
                    graph.add_edge(l2, l1, w)
        else:
            raise InvalidInputException("Invalid input type")
        return graph

    # TimeComplexity: O(V+E)
    # SpaceComplexity: O(V)    -- the 'path' storage
    def DFS(self, label:str, path:list[str] = []) -> list[str]:
        '''Depth First Search starting from given Vertex'''
        helper = GraphHelper(self)
        if label not in helper.namebook:
            raise InvalidInputException('label {} does not exist'.format(label))
        v = helper.namebook[label]
        path.append(label)
        for e in v.edges:
            if e.to and not helper.visited[e.to.label] and e.to.label not in path:
                self.DFS(e.to.label, path)
        helper.visited[label] = True
        return path

    def BFS(self, label:str, path:list[str] = [], helper:GraphHelper = None) -> list[str]:
        if not helper:
            helper = GraphHelper(self)
        if label not in helper.namebook:
            raise InvalidInputException('label {} not exist'.format(label))
        if label not in path:
            path.append(label)
        v = helper.namebook[label]
        for e in v.edges:
            if e.to and e.to.label not in path and not helper.visited[label]:
                path.append(e.to.label)
        helper.visited[label] = True

        for l in path:
            if not helper.visited[l]:
                self.BFS(l, path, helper)
        return path


    def topological_sort(self) -> list[str]:
        '''The topological sort of current graph 
           Assume there is no loop.
        '''
        path = []
        helper = GraphHelper(self)
        for v in self.vertices:
            path = self._topological_sort_func(v.label, path, helper)
        return path[::-1]  

    def _topological_sort_func(self, label:str, path:list[str] = [], helper:GraphHelper = None) -> list[str]:
        if not helper:
            helper = GraphHelper(self)
        if not label in helper.namebook:
            raise InvalidInputException('label {} not exist'.format(label))
        helper.visited[label] = True
        v = helper.namebook[label]
        for e in v.edges:
            if not helper.visited[label] and e.to.label not in path:
                self._topological_sort_func(e.to.label, path, helper)
        path.append(label)
        return path


class SimpleGraph(object):
    '''SimpleGraph, no weight, not directed'''
    def __init__(self) -> None:
        self.vertices = {}       # {'label1':['label11', 'label12', ..]}

    def add_adjacency(self, label1:str, label2:str, directional=True) -> None:
        if label1 in self.vertices:
            if label2 and label2 not in self.vertices[label1]:  # exist
                self.vertices[label1].append(label2)
        else:
            if label2:
                self.vertices[label1] = [label2]
                if label2 not in self.vertices:
                    self.vertices[label2] = []
            else:
                self.vertices[label1] = []
        if not directional:
            self.add_adjacency(label2, label1, True)

    @staticmethod
    def generate(data:dict[str:list[str]], directed=False) -> 'SimpleGraph':
        sg = SimpleGraph()
        for label, to in data.items():
            for l2 in to:
                sg.add_adjacency(label, l2, directional=directed)
        return sg

    def __str__(self) -> str:
        s = '{}\n'.format(type(self))
        for label, to in self.vertices.items():
            s = s + '{}: {}\n'.format(label, to)
        s = s + '\n'
        return s

    def DFS(self, label:str, path:list[str] = [], visited:list[bool] = None) -> list[str]:
        if label not in self.vertices:
            raise InvalidInputException()
        if not path:
            path = []
        if not visited:
            visited = {label:False for label in self.vertices}
        path.append(label)
        for to in self.vertices[label]:
            if to not in path and not visited[to]:
                self.DFS(to, path, visited)
        visited[label] = True
        return path

    def has_loop(self)->bool:
        for label in self.vertices:
            if self.loop_detect(label):
                return True
        return False

    def loop_detect(self, label:str=None, path:list=None, visited:list=None) -> bool:
        if None == path:
            path = []
        if None == visited:
            visited = {l:False for l in self.vertices}
        if label in path:
            return True
        path.append(label)
        for e in self.vertices[label]:
            if not visited[e]:
                if self.loop_detect(e, path, visited):
                    return True
        visited[label] = True
        path.pop()
        return False
           



GraphSampleData = {
    'LaneCove':[('Chatswood', 3), ('Epping', 10), ('Artarmon', 2), ('NorthSydney', 7), ('PennentHill', 26)],
    'Chatswood':[('LaneCove', 3), ('Sydney', 13), ('NorthSydney',8), ('PennentHill', 20)],
    'Artarmon':[('Chatswood', 1), ('NorthSydney',6)],
    'Epping':[('PennentHill', 17)],
    'BaukhamHills':[('Epping', 14), ('SevenHills', 8), ('PennentHill', 7)],
    'Sydney':[('Pyrmont', 2), ('NorthSydney',4), ('Epping', 20)],
}

def test():
    graph_data1 = { 'a':[('b',2), ('c',3), ('d',4)],
                   'e':[('f',12), ('g',3), ('h',4)],
                   'c':[('x',2), ('g',3), ('z',4)],
                   'x':[('y',2), ('z',3), ('a',14)],
                 }
    graph_data2 = [('a','b',2), ('a','c',3), ('a','d',4),
                   ('e','f',12), ('e','g',3), ('e','h',4),
                   ('c','x',2), ('c','g',3), ('c','z',4),
                   ('x','y',2), ('x','z',3), ('x','a',14)
                   ]

    g1 = Graph()
    g1 = Graph.generate(graph_data1, directed=False)
    print(g1)
    g2 = Graph()
    g2 = Graph.generate(graph_data2, directed=False)
    print(g2)

    ds = { 'a':['b', 'c', 'd'],
           'e':['f', 'g', 'h'],
           'c':['x', 'g', 'z'],
           'x':['y', 'z', 'a'],
        }
    sg = SimpleGraph.generate(ds)
    print(sg) 

    ###
    print('DFS')
    g = Graph.generate(GraphSampleData, directed=False)
    path = g.DFS('Chatswood')
    print(path)

    print('DFS (SimpleGraph)')
    path = sg.DFS('b')
    print(path)

    ###
    print('BFS')
    g = Graph.generate(GraphSampleData, directed=False)
    path = g.BFS('Chatswood')
    print(path)

    ###
    print('Topological Sort')
    project_depend_data = [('a', 'd', None), ('f', 'b', None), ('b', 'd', None), ('f', 'a', None), ('d', 'c', None), ('c', None, None)]
    g = Graph.generate(project_depend_data, directed=True)
    print(g)
    path = g.topological_sort()
    print(path)

    #
    print('simpleGrap loop')
    print(sg.has_loop())        # True
    ds2 = {
        1:[],
        2:[1],
        3:[1,2],
        4:[3, 6],
        5:[4,2],
        6:[3,1],
    }
    sg2 = SimpleGraph().generate(ds2, directed=True)
    print(sg2.has_loop())       # True
    ds3 = {
        1:[],
        2:[1],
        3:[1,2],
        4:[3, 1],
        5:[4,2,3],
        6:[3,4,2,1],
    }
    sg3 = SimpleGraph().generate(ds3, directed=True)
    print(sg3.has_loop())        # False



test()

