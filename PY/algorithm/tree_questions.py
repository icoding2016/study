# 4.2 Minimal Tree: 
# Given a sorted (increasing order) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height.

# 4.3 List of Depths: 
# Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
# Hints:

# 4.4 Check Balanced: 
# Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.
# Hints:
#   If a tree is balanced, all sub-trees balance 

# 4.5 Validate BST: 
# Implement a function to check if a binary tree is a binary search tree.
# Hints: 
#  

# 4.6 Successor: 
# Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.
# Hints: 

# 4.7 Build Order (*): 
# You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c
# Hints:
#   If p1 depend on p2 and p2 depend on p1, that's a loop -- Error.
#   For each project p, list its dependencies  [p:[<dependencies>]].
#     if p has no dependency, put it to the build_order list. (if p also has project depending on it, 
#       insert it to the head so it can be build earlier; otherwise append it to the tail) 
#     if p has dependencies, but the dependencies are all in build_order list, then dependency cleared, append it to build_order

# 4.8 First Common Ancestor: 
# Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. 
# NOTE: This is not necessarily a binary search tree.
# Hints: #

# 4.9 BST Sequences (**): 
# A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.
# EXAMPLE
# Input:
# Output: {2, 1, 3}, {2, 3, 1}
# Hints:
#   For each node, the data below it should come after current node.data, the sequence doen't matter.
#   So on each node, find all the combinitions of below nodes, and prefix with node.data
#   To find the combinations, get node.left's combination and right's, then weave them.

# 4.1 O Check Subtree: 
# Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
# algorithm to determine if T2 is a subtree of Tl.
# A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.
# Hints:

# 4.11 Random Node: 
# You are implementing a binary tree class from scratch which, in addition to
# insert, find, and delete, has a method getRandomNode() which returns a random node
# from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for getRandomNode, and explain how you would implement the rest of the methods.
# Hints: 
#   Solution:  it takes 1~logN steps to reach a node. To get equal choice, we take random(1, logN) steps 
#              and choose left or righ with 50% chance at each step

# 4.12 Paths with Sum: 
# You are given a binary tree in which each node contains an integer value (which
# might be positive or negative). Design an algorithm to count the number of paths that sum to a
# given value. The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).
# Hints:

# Find the min and max depth of a tree
# Given a tree, get the min and max depth.
# 



from typing import TypeVar
from typing import Union
from tree import BTree
from bdtree import BDTree

T = TypeVar('T')

class ErrorException(Exception):
    pass

class InvalidInputException(Exception):
    pass


def mini_tree(data:list[int]) -> BTree:
    '''Create a mini depth binary search tree from the data of a sorted list'''
    if len(data) < 1:
        return None
    if len(data) == 1:
        return BTree(data[0])
    mid = len(data)//2
    #print(mid)
    node = BTree(data[mid])
    node.left = mini_tree(data[:mid])
    node.right = mini_tree(data[mid+1:])
    return node


class LinkedNode(object):
    def __init__(self, data:T) -> None:
        self.data = data
        self.next = None

    def append(self, data:T) -> None:
        '''append a data to tail'''
        next = self.next
        cur = self
        while next:
            cur = next
            next = next.next
        cur.next = data

    def insert(self, data:T) -> T:
        '''insert the data in front of the head'''
        data.next = self
        return data

def list_of_depths(root:BTree, level:int = 0, lst:list[LinkedNode] = []) -> list[LinkedNode]:
    if not root:
        return lst
    if level >= len(lst):
        lst.append(LinkedNode(root))
    else:
        lst[level].append(LinkedNode(root))

    if root.left:
        list_of_depths(root.left, level + 1, lst)
    if root.right:
        list_of_depths(root.right, level + 1, lst)
    return lst


# balance: for each node 'left height == right hight'
# Time Complexity:   O(N)  --  the recursive call goes through every node once each. There are N node so N calls.
# Space Complexity:  O(H)  --  Note, not O(N). There recursive calls but they are not happening at the same time. 
#                              The left node recursive goes down to the end node (level H) while the right recursive calls 
#                              haven't happen yet; when the right calls happen, the left calls have done.
def check_balance(root:BTree) -> (bool,int):
    if root is None:
        return True, 0
    if root.left is None and root.right is None:
        return True, 1
    b1, h1 = check_balance(root.left)
    b2, h2 = check_balance(root.right)
    balance = (h1 == h2) and b1 and b2
    return balance, max(h1,h2)+1

# validate BST (Binary Search Tree)
# This solution is not correct. The key issue is, BST is not only left < current < right,
# but also all left nodes < all right nodes.
# Below algorithm only check 'left < current < right' for each node 
def validate_bst_1(root:BTree) -> bool:
    if not root:
        return True
    if root.left and root.left.value > root.value:
        return False
    if root.right and root.right.value < root.value:
        return False
    return validate_bst(root.left) and validate_bst(root.right)

# validate BST (Binary Search Tree)
# Check: 
#   1) left < current < max
#   2) max from left (and left-below) < current < min from right (and right-below)
#   The max/min value shoudl be carried from bottom to upper level. 
def validate_bst(root:BTree) -> (bool, int, int):
    if not root:
        return True, None, None
    if not root.left and not root.right:
        return True, root.value, root.value

    lb, l_min, l_max = validate_bst(root.left)
    rb, r_min, r_max = validate_bst(root.right)  

    l_min = l_min if l_min else root.value
    r_min = r_min if r_min else root.value
    l_max = l_max if l_max else root.value
    r_max = r_max if r_max else root.value

    return (lb and rb and l_max <= root.value and r_min >= root.value, 
           min(r_min, l_min), 
           max(l_max, r_max))


# Build dependency
# (p1,p2) the second project is dependent on the first project. 
# All of a project's dependencies must be built before the project
# Time Complexity:   O(P*D) ?? where P is project#, D is dependency#
# Space Complexity:
#  Note: Topological Sort Time Complexity is O(P+D)
def build_dependency(projects:list[str], dependencies:list[tuple]) -> list[str]:
    dependon = {x:[] for x in projects}
    dependby = {x:[] for x in projects}
    for x in dependencies:
        if x[1] in dependon:
            dependon[x[1]].append(x[0])     # { <proj>:[<dependency>,...]}
        if x[0] in dependby:
            dependby[x[0]].append(x[1])
    # check dependency loop
    for x in dependon:
        for y in dependon[x]:
            if x in dependon[y]:
                raise ErrorException('Error, dependency loop {}-{}'.format(x, y))
      
    build_order = []
    remain_projs = projects.copy()
    while remain_projs:
        for p in remain_projs:
            if not dependon[p]:  # no dependency
                if dependby[p]:
                    build_order.insert(0, p)
                else:
                    build_order.append(p)
            else:
                no_dependency = True
                for d in dependon[p]:
                    if d in build_order:
                        continue
                    else:
                        no_dependency = False
                        break
                if no_dependency:
                    build_order.append(p)
        remain_projs = [x for x in projects if x not in build_order]
    return build_order



def build_dependency_topo_sort(projects:list[str], dependencies:list[tuple]) -> list[str]:
    pass



# First Common Ancestor
def first_common_ancestor(node1:BDTree, node2:BDTree) -> BDTree:
    if not node1 or not node2:
        return None
    parents1 = []
    parents2 = []
    n1 = node1
    n2 = node2
    while n1.parent and n2.parent:
        if n1.parent:
            parents1.append(n1.parent)
        if n2.parent:
            parents2.append(n2.parent)
        if n1.parent in parents2:
            return n1.parent
        if n2.parent in parents1:
            return n2.parent
        n1 = n1.parent
        n2 = n2.parent
    return None

# BST Sequences
#   Not solved yet
# def bst_sequences(root:BTree) -> list[list[T]]:
#     if not root:
#         return []
#     if root.left:
#         ll = bst_sequences(root.left)
#     if root.right:
#         rr = bst_sequences(root.right)
    
#     combinations = weave(ll, rr)
#     for x in combinations:
#         x = [root.data] + x
#     return combinations

# # weave the 2 lists, keep data in relative order
# def weave(ll:list[list], rr:list[list]) -> list[list]:
#     if not ll:
#         return rr
#     if not rr:
#         return ll
#     if len(ll) <= 1 and len(rr) <= 1:
#         return [ll+rr, rr+ll]
#     newcomb = []
#     newcomb.extend(weave(ll[0], weave(ll[1:], rr)))
#     newcomb.extend(weave(rr[0], weave(rr[1:], ll)))
#     return newcomb
    

# Check Subtree
# Time Complexity:   O(H1 + N2)  if sorted tree   <- O(logN1) + O(N2)
#                    O(N1 + N2)  if not sortedtree <- O(N1) + O(N2)
# Space Complexity:  O(H1 + H2)  if sorted tree   <- O(logN1) + O(logN2)
#                    O(N1 + H2)  if not sorted    <- O(N1) + O(logN2)
def check_subtree(t1:BTree, t2:BTree) -> bool:
    if not t1 or not t2:
        raise InvalidInputException()
    r1 = t1.find_node(t2.value)
    return compare_tree(r1, t2)

def compare_tree(t1:BTree, t2:BTree) -> bool:
    if not t1 and not t2:
        return True
    if (not t1 and t2) or (t1 and not t2):
        return False

    result = compare_tree(t1.left, t2.left)
    if not result:
        return False
    result = compare_tree(t1.right, t2.right)
    if not result:
        return False
    return True

# path with sum
def path_with_sum(root:BTree, sum:int, cur_sum:int=0, cur_count:int=0, cur_path:list=None, paths:list[list]=None) -> (int, list):
    if not paths:
        paths = []
    if not cur_path:
        cur_path = []
    if not root:
        return cur_count, paths
    local_path = cur_path + [root.value]
    local_sum = cur_sum + root.value
    #print(local_sum)
    if local_sum == sum:
        cur_count += 1
        paths.append(local_path)

    if root.left:
        cur_count, paths = path_with_sum(root.left, sum, local_sum, cur_count, local_path, paths)
    if root.right:
        cur_count, paths = path_with_sum(root.right, sum, local_sum, cur_count, local_path, paths)

    return cur_count, paths

def tree_min_max_depth(tree:BTree) -> (int, int):
    """Given a binary tree, return min and max depth.

       dmin(node) = min(dmin(left), dmin(right))+1 if left and right 
                    dmin(left)+1 if left and not right
                    dmin(right)+1 if right and not left
                    1 if not left and not right
       dmax(node) = max(dmax(left) if left else 0, dmax(right) if right else 0) + 1
    """
    dmin_l, dmax_l = tree_min_max_depth(tree.left) if tree.left else (0, 0)
    dmin_r, dmax_r = tree_min_max_depth(tree.right) if tree.right else (0, 0)
    dmax = max(dmax_l, dmax_r)+1
    if not tree.left and not tree.right:
        dmin = 1
    elif tree.left and not tree.right:
        dmin = dmin_l + 1
    elif tree.right and not tree.left:
        dmin = dmin_r + 1
    else:
        dmin = min(dmin_l, dmin_r) + 1
    return dmin, dmax
    



def test():
    data = [1,2,3,4,5,6,7,8,9,10]
    node = mini_tree(data)
    print("tree hight:", BTree.hight(node))
    BTree.print_tree(node)

    # list of depths
    lst = list_of_depths(node)
    for i in range(len(lst)):
        node = lst[i]
        s = ''
        while node:
            s = s + '{},'.format(node.data.value)
            node = node.next
        #print("level {}: {}".format(i, s))


    # check balance
    print('-- Check balance --')
    node = mini_tree([1])
    print(check_balance(node))   # True
    node = mini_tree([1,2,3])   
    print(check_balance(node))   # True
    node = mini_tree([1,2,3,4,5,6])   
    print(check_balance(node))   # False
    node = mini_tree([1,2,3,4,5,6,7])   
    print(check_balance(node))   # True
    node = mini_tree([1,2,3,4,5,6,7,8,9])   
    print(check_balance(node))   # False
    node = mini_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])   
    print(check_balance(node))   # True

    # validate BST
    print('-- Validate BST --')
    node = mini_tree([1,2,3,4,5,6])   
    print(validate_bst(node))   # True
    node = mini_tree([10, 1,2,3,4,5,6])   
    print(validate_bst(node))   # False
    node = BTree.generate([20,10,30,5,15,3,7,15,17])
    print(validate_bst(node))   # True

    # build dependency
    print("-- Build dependency --")
    projects = ['a','b','c','d','e','f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    print(build_dependency(projects, dependencies))    # f, e, a, b, d, c

    # first_common_ancestor
    print('first_common_ancestor')
    data = [7,5,15,2,6,13,3,4,9,1,11,8,10,0,14,12]
    tree = BDTree.generate(data)
    print(tree)
    node1 = tree.get_node(data=13)
    node2 = tree.get_node(data=9)
    node = first_common_ancestor(node1, node2)
    print(node.data)

    # check_subtree
    print('check_subtree: ', end='')
    data1 = [20,10,50,7,13,36,98,4,8,12,17,28,44,80,127,2,5,9,6,60,79,1]
    data2 = [4,5,2,6,1]
    t1 = BTree.generate(data1)
    t2 = BTree.generate(data2)
    print(check_subtree(t1, t2))
    t3 = BTree.generate(data2, sorted=False)
    print(check_subtree(t1, t3))

    # path_with_sum
    print('path_with_sum')
    t = BTree.generate([10,5,15,3,8,12,19,2,4,6,9,0,1,7])
    print(path_with_sum(t, 20))
    t2 = BTree.generate([2,1,3,1,2,1,3,1,1,3,1,2,1,3,1,1,1,1,2,1])
    print(path_with_sum(t2, 5))

    # tree_min_max_depth
    print('tree_min_max_depth')
    t = BTree.generate([10,5,15,3,8,12,19,2,4,6,9,0,1,7])
    print(t)
    print(tree_min_max_depth(t))
    t = BTree.generate([7,4,10,2,5,8,9])
    print(t)
    print(tree_min_max_depth(t))



test()