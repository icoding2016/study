# Course Schedule
# Medium
# There are a total of num prerequisites you have to take, labeled from 0 to numCourses-1.
# Some prerequisites may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of prerequisites and a list of prerequisite pairs, is it possible for you to finish all prerequisites?

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 prerequisites to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 prerequisites to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Constraints:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5
#
# Ideas:
#   Solution 1: 
#     For each course, list the dependencies, go through the list/dependencies to check if all course can be arranged.
#   Solution 2: 
#     Loop detection.  
#   

from collections import defaultdict
from call_counter import call_counter, show_call_counter


# T(n^2)  -> each round at lease arrange a course (otherwise return False), so the loop decreases. 
#            n + (n-1) + .. + 1 = n*(n+1)/2
def courses_bf(prerequisites:list[list]) -> bool:
    if not prerequisites:
        return True
    cd = defaultdict(list)
    for c, d in prerequisites:
        cd[c].append(d)
        cd[d].extend([])   # note: this is necessary

    arranged = []
    num = len(cd)
    while num > 0:
        new_arranged = []
        for c, ds in cd.items():
            if not ds:
                arranged.append(c)
                new_arranged.append(c)
                continue
            has_dep = False
            for d in ds:
                if d not in arranged:
                    has_dep = True
                    break
            if not has_dep:
                arranged.append(c)
                new_arranged.append(c)
                continue
        for a in new_arranged:
            cd.pop(a)
        if num == len(cd):
            return False
        num = len(cd)
    return True


# T(n^2) 
def courses_noloop(prerequisites:list[list]):
    cd = defaultdict(list)
    for c, d in prerequisites:
        cd[c].append(d)
        cd[d].extend([])
    
    for c in cd:
        if detect_loop(cd, c):
            return False
    show_call_counter()
    return True

@call_counter
def detect_loop(cd:defaultdict, c:int, path:list=None) -> bool:
    if None == path:
        path = []

    if c in path:
        return True
    for d in cd[c]:
        if detect_loop(cd, d, path+[c]):
            #print('visited loop {} in {}'.format(d, path))
            return True
    return False



# T(N*(N+E)) ?  -> 1st loop O(N), then for each node in the 1st loop, do dfs O(V+E) -> O(N+E).
#                  so total:  O(N*(N+E)) 
def courses_noloop2(prerequisites:list[list]):
    cd = defaultdict(list)
    for c, d in prerequisites:
        cd[c].append(d)
        cd[d].extend([])

    for c in cd:
        if detect_loop2(cd, c):
            return False
    show_call_counter()
    return True

@call_counter
def detect_loop2(cd:defaultdict, c:int, visited:dict=None, path:list=None) -> bool:
    if None == path:
        path = []
    if None == visited:
        visited = {c:False for c in cd}

    if c in path:
        return True
    for d in cd[c]:
        if not visited[d]:
            if detect_loop2(cd, d, visited, path + [c]):
                return True
    visited[c] = True 
    return False


def test_func(f):
    print(f.__name__)
    c = [[1,0]]
    print(c, ' -> ', f(c))              # True
    c = [[1,0], [0, 1]]
    print(c, ' -> ', f(c))              # False
    c = [[1,0], [2, 1], [3, 2], [4, 2], [3,1],[3,0]]
    print(c, ' -> ', f(c))              # True
    c = [[1,0], [2, 1], [3, 2], [4, 2], [0, 3]]
    print(c, ' -> ', f(c))              # False
    c = [[2,0],[1,0],[3,1],[3,2],[1,3]]
    print(c, ' -> ', f(c))              # False
    



def test():
    test_func(courses_bf)
    test_func(courses_noloop)
    test_func(courses_noloop2)




test()
