# Minimum Distance Between Words of a String
# Given a string s and two words w1 and w2 that are present in S. 
# The task is to find the minimum distance between w1 and w2. 
# Here distance is the number of charactors between the 2 words.
# 
# Examples:
# Input : s = “geeks for geeks contribute practice”, w1 = “geeks”, w2 = “practice” 
# Output : 12 
# 
# Input : s = “test frog, the quick the brown quick brown the frog”, w1 = “quick”, w2 = “frog” 
# Output : 6
#

class WordMissingException(Exception):
    pass


class Solution(object):
    def __init__(self)->None:
        pass

    def min_distance(self, words:str, w1:str, w2:str)->int:
        return self.min_distance1(words, w1, w2)

    def min_distance1(self, words:str, w1:str, w2:str)->int:
        pre_ie = None
        pre_w = None
        min_gap = len(words)+1
        w = None
        i = 0
        while i < len(words)-min(len(w1), len(w2)):
            if self.match_word(words,i,w1):
                w = w1
            elif self.match_word(words,i,w2):
                w = w2
            else:
                i += 1
                continue
            if pre_w and pre_w != w:
                min_gap = min(i-pre_ie, min_gap)
            pre_w, pre_ie = w, i+len(w)
            i += len(w)
        return min_gap

    def match_word(self, words:str, i:int, w:str)->list:
        if i+len(w) > len(words):
            return False
        return words[i:i+len(w)] == w

    


def test_fixture(solution):
    testdata = [  # (input, expect),
        (("geeks for geeks contribute practice", "geeks", "practice"), 12),
        (("test frog, the quick the brown quick brown the frog", "quick", "frog"), 6),
        (("bar and foo: test to check foo distance to bar with multi foo and multi bar in str", "foo", "bar"), 5),
        (("another foo / bar test where min foo, bar namely the foo and the bar distance is 0", "foo", "bar"), 2),
    ]

    for i in range(len(testdata)):
        ret = solution.min_distance(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))



def test():
    s = Solution()
    test_fixture(s)


test()    
