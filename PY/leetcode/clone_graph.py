# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
#
# Test case format:
# For simplicity sake, each node's value is the same as the node's index (1-indexed). 
# For example, the first node with val = 1, the second node with val = 2, and so on. 
# The graph is represented in the test case using an adjacency list.
# Adjacency list is a collection of unordered lists used to represent a finite graph. 
# Each list describes the set of neighbors of a node in the graph.
# The given node will always be the first node with val = 1. 
# You must return the copy of the given node as a reference to the cloned graph.
#
# Example 1:
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
#
# Example 2:
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
#
# Example 3:
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
#
# Example 4:
# Input: adjList = [[2],[1]]
# Output: [[2],[1]]
#
# Constraints:
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# Number of Nodes will not exceed 100.
# There is no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.

# Note:
#   The key for the recursive clone solution is:  
#     The new node need to be created first before recursion.
#     otherwise, it always rely on creating the neighbor nodes first; when there are loops, it will loop indefinitly


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []   # [Node1, Node2, ..]

    @staticmethod
    def create(adjlist:list['Node'], val:int=1, nodes:dict=None) -> 'Node':
        if None == nodes:
            nodes = dict()       #{val:node_obj}
        if val > len(adjlist):
            return None

        if val in nodes:
            return nodes[val]
        neighbors = []
        cur_node = Node(val, neighbors)     # have to create the node first, the update neighbors
        nodes[val] = cur_node
        for i in adjlist[val-1]:
            # if i in {n.val:n for n in neighbors}:
            #     continue
            if i in nodes:
                nn = nodes[i]
            else:
                nn = Node.create(adjlist, i, nodes)
            neighbors.append(nn)
        # update neighbors
        cur_node.neighbors = neighbors
        return cur_node
    
    def dfs(self, path:list=None, visited:dict=None)->None:
        if None == path:
            path = []
        if None == visited:
            visited = dict()
        
        if self.val in visited:
            return
        path.append(self.val)
        yield self
        for n in self.neighbors:
            if n.val in visited or n.val in path:
                continue
            for x in n.dfs(path, visited):
                yield x
        visited[self.val]=True
        path.pop()


    def show(self):
        nodes = {}
        for n in self.dfs():
            nodes[n.val] = {x.val for x in n.neighbors}
        result = [nodes[i] for i in range(1, len(nodes)+1)]
        print(result)



#
def clone_graph(node: 'Node', nodes:dict=None) -> 'Node':
    if None == nodes:
        nodes = dict()
    neighbors = []
    if node.val not in nodes:
        cnode = Node(node.val, [])
        nodes[node.val] = cnode
    nn = None
    for n in node.neighbors:
        if n.val in nodes:
            nn = nodes[n.val]
        else:
            nn = clone_graph(n, nodes)
        if n.val not in {x.val:x for x in neighbors}:
            neighbors.append(nn)
    cnode.neighbors = neighbors
    return cnode
        
def test_func(f):
    adj = [[2,4],[1,3],[2,4],[1,3]]
    g = Node.create(adj)
    g.show()
    g2 = f(g)
    g2.show()


def test():
    test_func(clone_graph)


test()
