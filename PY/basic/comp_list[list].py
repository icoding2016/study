#  compare if two list[list, ] are the same, order doesn't matter
#  e.g.  below 2 list are considered as 'Equal'
#    [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']]
#    [['tea', 'ate', 'eat'], ['bat'], ['nat', 'tan']]  
# 
# 
#  #

class Solution():
    def comp_list_list(self, l1:list[list], l2:list[list])->bool:
        if len(l1) != len(l2):
            return False       
        ls1 = [set(x) for x in l1]
        ls2 = [set(x) for x in l2]
        if len(ls1) != len(ls2):
            return False       
        while len(ls1):
            s = ls1[0]
            if s in ls2:
                ls1.remove(s)
                ls2.remove(s)
            else:
                return False
        if not ls1 and not ls2:
            return True
        else:
            return False


def test_fixture(solution):
    testdata = [  # (input, expect),
        (([], []), True),
        (([[],[""]], [[],[""]]), True),
        (([["a"], ["b"]], [["b"], ["a"]]), True),
        (([["a"], ["b"], []], [["b"], ["a"]]), False),
        (([["a"], ["b"], ["cc"]], [["b"], ["a"],["c"]]), False),
        (([["a","b"],["c","d"]], [["d","c"],["b","a"]]), True),
        (([['tea', 'ate', 'eat'], ['bat'], ['nat', 'tan']], [["bat"],["nat","tan"],["ate","eat","tea"]]), True),
        (([['tea', 'ate', 'eat'], ['bat'], ['nat', 'tan']], [["bat"],["nat","tan","atn"],["ate","eat","tea"]]), False),
    ]

    for i in range(len(testdata)):
        ret = solution.comp_list_list(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \n\t{} \t\t{} expect {}".format(testdata[i][0], ret, 'pass' if ret==exp else 'fail', exp))



def test():
    s = Solution()
    test_fixture(s)


test()    


