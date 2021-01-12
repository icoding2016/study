# Minimum Distance Between Words of a String
# Given a string s and two words w1 and w2 that are present in S. 
# The task is to find the minimum distance between w1 and w2. 
# Here distance is the number of steps or words between the first and the second word.
# https://www.geeksforgeeks.org/minimum-distance-between-words-of-a-string/ 
# 
# Examples:
# Input : s = “geeks for geeks contribute practice”, w1 = “geeks”, w2 = “practice” 
# Output : 1 
# There is only one word between closest occurrences of w1 and w2.
# Input : s = “the quick the brown quick brown the frog”, w1 = “quick”, w2 = “frog” 
# Output : 2
#

class WordMissingException(Exception):
    pass


class Solution(object):
    def __init__(self)->None:
        pass

    def min_distance(self, words:str, w1:str, w2:str)->int:
        #return self.min_distance_bf(words, w1, w2)
        return self.min_distance1(words, w1, w2)

    def min_distance1(self, words:str, w1:str, w2:str)->int:
        wl = words.split(" ")
        min_d = len(wl)+1
        pre_i=None
        pre_w=None
        for i,w in enumerate(wl):
            if w in [w1, w2]:
                if not pre_w:
                    pre_w = w
                    pre_i = i
                    continue
                else:
                    if pre_w == w:
                        pre_i = i
                        continue
                    else:
                        min_d = min(min_d, i-pre_i)
        return min_d-1

    def find_word(self, words:str, w:str)->list:
        result = []
        wl = words.split(" ")
        for i, x in enumerate(wl):
            if x == w:
                result.append(i)
        return result

    # T(N*L + W1*W2)   W1:w1#, W2:w2#,  N*L (L=max(len(w1),len(w2)))
    def min_distance_bf(self, words:str, w1:str, w2:str)->int:
        # get index
        w1s = self.find_word(words, w1)
        w2s = self.find_word(words, w2)

        min_gap = None
        for i in w1s:
            for j in w2s:
                gap = abs(i-j)
                min_gap = gap if not min_gap else min(min_gap, gap)
        return min_gap-1

    # wrong
    def min_distance2(self, words:str, w1:str, w2:str)->int:
        # get index
        w1s = self.find_word(words, w1)
        w2s = self.find_word(words, w2)

        if not w1s or not w2s:
            raise WordMissingException()
        
        left = w1s if w1s[0] < w2s[0] else w2s
        right = w2s if left == w1s else w1s
        i = 0
        j = len(right)-1
        min_gap = abs(left[i]-right[j])
        while i <= len(left):
            min_gap = min(min_gap, abs(left[i]-right[j]))
            while 0<=j and abs(left[i]-right[j]) >= min_gap:
                j -= 1
            if j >= 0:
                min_gap = abs(left[i]-right[j])
            i += 1
        return min_gap - 1



def test_fixture(solution):
    testdata = [  # (input, expect),
        (("geeks for geeks contribute practice", "geeks", "practice"), 1),
        (("the quick the brown quick brown the frog", "quick", "frog"), 2),
        (("bar and foo test to check foo distance to bar with multi foo and multi bar in str", "foo", "bar"), 1),
        (("another foo and bar test where min foo bar namely the foo and the bar distance is 0", "foo", "bar"), 0),
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
