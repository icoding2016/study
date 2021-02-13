# define the number of stops the elevator will take to carry N persons to F floors and then the elevator returns to lvl0.
# The persons (weight W=[W1,W2, ..]) start from floor 0 and will go to floor per F=[lvl, ]
# The max number of people in elevator is M, max load L.
# What is the min stops?  (-1 if impossible)
#
# e.g.
# W = [60, 80, 40] weight of each person
# F = [2, 3, 5] floor
# M = 2 (max number of people in the elevator)
# L = 200 (max load of the elevator)
# For this case the solution would be N = 5, 
# since the elevator took 60 plus 80 to floors number 2 and 3 (2 stops), then came back to 0 (3 stops), 
# it went to 5 (4 stops) and it returned to 0 ( 5 stops).
# 
# 
# Thoughts:
#   - try carry as many of persons in on round trip
#   - try to group the persons with same dest level
#   but that may not help in the software solution, we still need go through combinations. 
#
# Solution 1:  list permutations, then group by order
# Solution 2:  pick combinations as group 
# 
# #


class Elevator(object):
    def __init__(self, maxPersons=10, maxLoad=1000):
        self.maxPersons = maxPersons
        self.maxLoad = maxLoad

    def minStops(self, weights:list, floors:list, N:int=None, L:int=None )->int:
        if max(weights) > self.maxLoad:
            return -1
        self.weights = weights
        self.floors = floors
        if N:
            self.maxPersons = N
        if L:
            self.maxLoad = L

        return self.minStops_bf(weights, floors)

    def minStops_bf(self, weights:list, floors:list)->int:
        #print([s for s in self.perms([i for i in range(len(self.weights))])])
        return min([s for s in self.perms([i for i in range(len(self.weights))])])

    # solution 1: list all permutations, for each permutation, group persons in order.
    #             con: duplicates
    # T(n!)  
    def perms(self, remain:list, cur:list=None)->None:  #->(list,int):
        if None == cur:
            cur = []

        if not remain:
            sect = []
            stop = 0
            #print(cur)
            while cur:
                w_remain = self.maxLoad - sum([self.weights[i] for i in sect])
                if len(sect) < self.maxPersons and cur[0] <= w_remain:
                    sect.append(cur.pop())
                    if cur:
                        continue
                stop += len({self.floors[i]:True for i in sect}) + 1 if sect else 0
                #print(sect, stop)
                sect.clear()
            yield stop    #perms, stops
            return

        for i, x in enumerate(remain):
            for s in self.perms(remain[:i]+remain[i+1:], cur+[x]):
                yield s
        return

    def combs(self, remain:list, cur:list=None)->None:
        if None == cur:
            cur = []
        





def test_fixture(s):
    testdata = [  # (input, expect),
        (([60,80,40], [2,3,5], 2, 200, ), 5),
        (([60,80,130,110], [2,3,5,2], 3, 200, ), 5),
   ]

    for i in range(len(testdata)):
        ret = s.minStops(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))


import timeit
def test():
    s = Elevator()
    test_fixture(s)

test()

