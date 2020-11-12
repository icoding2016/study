# Graph exercise
# 
# DFS:  Use a list (to record path). Recursive.
#       On each node: 
#         Add current node to path;
#         visit edge-nodes unless the node is visited (=all done on that node), 
#         when all edge-nodes are visited, mark current node visited, and return;
#         Note: when recurse edge-nodes, the one in the path has to be skipped (to avoid loop)
#
# BFS: Use a list (Queue) to record path.
#      The Queue is used to record the edge nodes under current node (breadth first, then need bfs for each of them later) 
#       On each node:
#         Add current node to path list (Queue)
#         iterate all edge-nodes in current node and save them to path (except those already saved)
#         when all edge-nodes were visited, mark current node as 'visited'
#         go back to the path list, pick next 'un-visited' node, repeat the bfs
#
# Path Finding (from A to B)
#       On each node (Recursively)
#          Push the node into current Path ('path')
#          If current node is already B (found), record current path. then move one node backward (Pop the node from path and return)
#          If current node is not B, go through all adjacencies (iteration).
#            Skip the adjacenct node that is already in the path (avoid loop)
#            Skip the adjacenct node that is 'visited' 
#            Do the same path find call to the adjacent node.
#            If all adjacenct node finished, mark current node 'visited', then move backward (pop it from path and return)
#       Note: 
#         1) this is path finding not bfs, so a node could be re-visited from other path options. 
#            So we clear 'visited' flag for the node's adjacencies after current round of iteration.
#         2) Pop current node from the path (go backward) when the search on this node finish
#
# SP (Short Path):
#      Starting from the 1st node, iterate possible paths to 2nd node (visiting each adjacent node recursively)
#      Record path-hops and cost (sum) for each path found
#        For each node: 
#          Check 'reaching dest': 
#            if yes, record current path, move backward for next adjacent, 
#            if no, go through adjacencies with 'find_paths_cost' call. (skip the visited and those already in current path). 
#            when all adjacencies checked, clear adjacencies' visited flag, and mark current node visited then go backwards.
#         
# Questions
# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.
# 
# 
# 4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
# to create a binary search tree with minimal height.
# 
# 
# 4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
# 
# 4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.
# Hints:#27, #33, #49, #705, #724
# 4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
# Hints: 
#  
# 
# 4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.
# Hints: 
#  
# 
# 4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c
# Hints:
#  
# 4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.
# Hints: 
#
# 4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.
# 
# 4.1O Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
# algorithm to determine if T2 is a subtree of Tl.
# A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.
# Hints:
# 
# 4.11 Random Node: You are implementing a binary tree class from scratch which, in addition to
# insert, find, and delete, has a method getRandomNode() which returns a random node
# from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for getRandomNode, and explain how you would implement the rest of the methods.
# Hints: 
#  
# 4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value (which
# might be positive or negative). Design an algorithm to count the number of paths that sum to a
# given value. The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).
# Hints: 


class NotExistException(Exception):
    pass

class AlreadyExistException(Exception):
    pass


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.edges = []
        self.visited = False

class Edge(object):
    def __init__(self, to, weight):
        self.to = to    # label
        self.weight = weight


class Graph(object):
    def __init__(self):
        self.vertices = []

    def __str__(self):
        s = ''
        for v in self.vertices:
            s += "{:<16}: ".format(v.label)
            for e in v.edges:
                to = "->{}({}),".format(e.to, e.weight)
                s += "{:20}".format(to)
            s += "\n"
        return s

    @staticmethod
    def generate(data: dict[str:tuple], directed):
        ''' { 'vertex_label11':('vertex_label12', weight), 
              'vertex_label21':('vertex_label22', weight), }
        '''   
        G = Graph()
        for l1, lst in data.items():
            for e in lst:
                G.add_edge(l1, e[0], directed, e[1])
        return G

    def add_vertex(self, label):
        v, _ = self.find_vertex(label)
        if v:
            raise AlreadyExistException("Vertex already exist.")
        v = Vertex(label)
        self.vertices.append(v)
        return v

    def add_edge(self, label1, label2, directed, weight):
        ''' Add edge to vertex,
            If vertex not exist, then create first
        '''
        v1, _ = self.find_vertex(label1)
        if not v1:
            v1 = Vertex(label1)
            self.vertices.append(v1)
            #print("create Vertex: {}".format(v1.label))

        found = False
        for e in v1.edges:
            if e.to == label2:       # exist
                e.weight = weight    # update weight
                found = True
                break
        if not found:
            e = Edge(label2, weight)
            v1.edges.append(e)
            #print("created edge: {}{}{}({})".format(v1.label, '->' if directed else '<->',label2, weight))
        
        if not directed:
            self.add_edge(label2, label1, True, weight)

    def find_vertex(self, label):
        for i, v in enumerate(self.vertices):
            if v.label == label:
                return v, i
        return None, None

    def find_edge(self, label1, label2, directed):
        '''
            return: [ (e1,v1),... ]
        '''
        v1, _ = self.find_vertex(label1)
        if not v1:
            return False
        ret = []
        for e in v1.edges:
            if e.to.label == label2:
                ret.append((e, v1))
                break
        if directed:
            return ret
        v2, _ = self.find_vertex(label2)
        if v2:
            for e in v2.edges:
                if e.label == label1:
                    ret.append((e, v2))
        return ret

    def sweep_vertex(self):
        '''Clean the visited flag'''
        for v in self.vertices:
            v.visited = False

    def show(self):
        print(self)

    def diameter(self, label1, label2):
        '''Get the diameter (the length of the longest path among all the shortest path) that link any two nodes
        '''
        pass

    def dfs(self, label: str, path: list =None) -> list:
        '''Depth First Search
          Arg:
            label: the starting node
            return: the path
        '''
        v, _ = self.find_vertex(label)
        if not v:
            raise NotExistException("Cannot find the starting node.")
        if not path:
            path = []
        path.append(v.label)
        for e in v.edges:
            ev, _ = self.find_vertex(e.to)
            if not ev:
                continue
            if ev.visited:  #skip
                continue
            if e.to not in path:
                self.dfs(e.to, path)
        v.visited = True
        return path


    def bfs(self, label: str, path: list = None) -> list:
        '''Breadth First Search
          Arg:
            label: the starting node
            return: the path
        '''
        v, _ = self.find_vertex(label)
        if not v:
            raise NotExistException("Cannot find the node {}".format(label))
        if not path:
            path = []

        if label not in path:
            path.append(label)

        for e in v.edges:
            ev, _ = self.find_vertex(e.to)
            if not ev:
                continue
            if ev.label not in path:
                path.append(ev.label)
        v.visited = True

        #print(path)
        for qlabel in path:     # Note: the path could have been updated by the bfs() call in the loop
                                #       but that's ok in Python, the 'for' iteration with follow the updated path
            uv, _ = self.find_vertex(qlabel)
            if uv and uv.visited:
                continue
            self.bfs(uv.label, path)

        return path

    def find_paths(self, label1, label2, found_paths, path=None):
        ''' Find path from label1 to label2
          retrun: [[path1], [path2], ..]     each path [label1, label_x..., label2]
        '''
        if not path:
            path = []

        v1, _ = self.find_vertex(label1)
        v2, _ = self.find_vertex(label2)
        if not v1 or not v2:
            raise NotExistException("Node not exist")
        
        path.append(label1)
        #print("path node push {}".format(label1))
        if label1 == label2:  # found
            if found_paths is None:
                found_paths = []
            found_paths.append(path.copy())
            #print(found_paths)
            path.remove(label1);   #print("path node pop {}".format(label1))
            return
        if not v1.edges:
            path.remove(label1)
            #print("path node pop {}".format(label1))
            return
        # iterate all adjacencies (edge-nodes)
        for e in v1.edges:
            ev, _ = self.find_vertex(e.to)
            if not ev:
                continue
            if ev.label in path:
                continue
            if not ev.visited:
                self.find_paths(ev.label, label2, found_paths, path)
        v1.visited = True
        # clear visited flag for edge nodes
        for e in v1.edges:
            ev, _ = self.find_vertex(e.to)
            ev.visited = False
        path.remove(v1.label);      # print("path node pop {}".format(label1))
        return

    class PathInfo(object):
        def __init__(self):
            self.path = []
            self.cost = []
            self.total_cost = 0

        def add_hop(self, label, cost):
            self.path.append(label)
            self.cost.append(cost)
            self.total_cost += cost
            #print("add hop: {}".format(label))

        def pop(self):
            v = self.path.pop(len(self.path)-1)
            self.total_cost -= self.cost.pop(len(self.cost)-1)
            #print("pop node: {}".format(v))
            return v

        def copy(self):
            new_path = Graph.PathInfo()
            new_path.path = self.path.copy()
            new_path.cost = self.cost.copy()
            new_path.total_cost = self.total_cost
            return new_path

        def show(self):
            for i in range(len(self.path)):
                print("{}({}) - ".format(self.path[i], self.cost[i]), end='')
            print(" total_cost=", self.total_cost)

    def find_paths_cost(self, label1, label2, weight=0, paths=None, path=None):
        '''Get the shortest distance between 2 given vertices'''
        v1, _ = self.find_vertex(label1)
        v2, _ = self.find_vertex(label2)
        if not v1 or not v2:
            raise NotExistException("Node not exist")
        
        if paths is None:
            paths = []    # [PathInfo1, PathInfo2, ...]
        if path is None:
            path = Graph.PathInfo()

        path.add_hop(label1, weight)
        small=None; sp=None

        if label2 == label1:
            paths.append(path.copy())
            path.pop()
            for p in paths:
                if not small:
                    small = p.total_cost
                elif small > p.total_cost:
                    small = p.total_cost
                    sp = p.path
            return small, sp

        for e in v1.edges:
            ve, _ = self.find_vertex(e.to)
            if not ve:
                continue
            if ve.label in path.path:
                continue
            if not ve.visited:
                self.find_paths_cost(ve.label, label2, e.weight, paths, path)
        v1.visited = True
        for e in v1.edges:
            ev, _ = self.find_vertex(e.to)
            if ev:
                ev.visited = False
        path.pop()


    def shortest_path(self, label1, label2):
        paths = []
        self.find_paths_cost(label1, label2, paths=paths)
        small = None
        sp = None
        for p in paths:
            if not small:
                small = p.total_cost
            elif small > p.total_cost:
                small = p.total_cost
                sp = p.path
        return small, sp, paths




def test_dfs(G):
    G.sweep_vertex()
    node='Chatswood'
    path = G.dfs(node)
    print("DFS ({}):".format(node), path)

def test_bfs(G):
    G.sweep_vertex()
    path = G.bfs(node)
    print("BFS ({}):".format(node), path)

def test_findpaths(G, l1, l2):
    G.sweep_vertex() 
    paths = []
    G.find_paths(l1,l2, found_paths=paths, path=None)
    print("Find paths from {} to {}:".format(l1, l2))
    if paths:
        for p in paths:
            print(p)
    else:
        print("not found")

def test_short_paths(G, l1, l2):
    G.sweep_vertex() 
    c, sp, paths = G.shortest_path(l1,l2)
    print("Shortest paths from {} to {}:".format(l1, l2), "cost: {}".format(c))
    for p in paths:
        p.show()
    


def test():
    data = {
        'LaneCove':[('Chatswood', 3), ('Epping', 10), ('Artarmon', 2), ('NorthSydney', 7), ('PennentHill', 26)],
        'Chatswood':[('LaneCove', 3), ('Sydney', 13), ('NorthSydney',8), ('PennentHill', 20)],
        'Artarmon':[('Chatswood', 1), ('NorthSydney',6)],
        'Epping':[('PennentHill', 17)],
        'BaukhamHills':[('Epping', 14), ('SevenHills', 8), ('PennentHill', 7)],
        'Sydney':[('Pyrmont', 2), ('NorthSydney',4), ('Epping', 20)],
    }

    G = Graph.generate(data, directed=False)
    print(G)

    #test_dfs(G)
    #test_bfs(G)
    #test_findpaths(G, l1 = "Epping", l2="Sydney")
    test_short_paths(G, l1 = "Epping", l2="Sydney")
    #test_short_paths(G, l1 = "BaukhamHills", l2="Pyrmont")


test()
