"""
127. Word Ladder
Hard
https://leetcode.com/problems/word-ladder/

A transformation sequence from word beginWord to word endWord using a dictionary 
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, 
return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.


Solutions:
  1. recursion + memorize
     memo(begin, end) = min( ladderLength(nexthop, end)+1, memo(begin, end) )
  2. SPF (Dijkstra)


"""

from collections import Counter
from sys import maxsize
from typing import List
from functools import lru_cache
from utils.testtools import test_fixture

_MAX = maxsize

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # return self.ladderLength_1(beginWord, endWord, wordList)
        return self.ladderLength_spf(beginWord, endWord, wordList)


    # SPF (Djikstra)
    # Djikstra TimeComplexity:  (V+E)logV (heap solution),   (V+E)*V (array solution)
    #   In this question,    E is V*(V-1) so about V*V,  so it's V*VlogV or V^3
    #   In this implementation: V^3,   considering O(L) L=len(word)  for wordDiff, => O(V^3*L)
    def ladderLength_spf(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        path = [beginWord]
        if endWord not in wordList or beginWord == endWord:
            return 0
        costs = {w:_MAX for w in wordList if w!=beginWord}
        found = False
        for w in wordList:
            if self.wordDiff(beginWord, w) == 1:
                costs[w] = 1
                found = True
        if not found:
            return 0
        if costs[endWord] == 1:
            return 1
        
        queue = [w for w in costs]
        while queue:
            w = min([k for k in costs if k in queue], key=lambda x:costs[x])
            if w == endWord:
                path.append(w); #print(path)
                return costs[w]+1 if costs[w]!=_MAX else 0
            for w2 in wordList:
                if w2 == beginWord or w2 == w:
                    continue
                if self.wordDiff(w, w2) == 1:
                    costs[w2] = min([costs[w2], costs[w]+1])
            queue.remove(w)
            path.append(w)
        #print(path)
        return costs[endWord]+1 if costs[endWord] != _MAX else 0

    # @lru_cache
    def wordDiff(self, word1:str, word2:str) -> int:
        if not hasattr(self, 'diffmemo'):
            self.diffmemo = {}
        key = tuple([word1, word2])
        if key in self.diffmemo:
            return self.diffmemo[key]
        c1 = Counter(word1)
        c2 = Counter(word2)
        diff = 0
        for w in c1:
            if w in c2:
                diff += abs(c1[w] - c2[w])
            else:
                diff += c1[w]
        self.diffmemo[key] = diff
        return diff

    # DFS + memorize
    # O(V*(V+E)*L)    L=len(word),  O(V) for each word as next starting point, O(V+E) for DFS for each starting point,  L for wordDiff()
    def ladderLength_1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.memo = {}  #
        return self.ladderLength_r(beginWord, endWord, wordList)

    def ladderLength_r(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        if self.wordDiff(beginWord, endWord) == 1:
            self.memo[(beginWord, endWord)] = 1
            return 1
        for i, w in enumerate(wordList):
            if w == beginWord:
                continue
            if self.wordDiff(beginWord, w) == 1:
                nextLength = self.ladderLength_r(w, endWord, wordList[:i]+wordList[i+1:])
                self.memo[(beginWord, endWord)] = min([nextLength+1, self.memo[(beginWord, endWord)]]) if (beginWord, endWord) in self.memo else nextLength+1
        return self.memo[(beginWord, endWord)] if (beginWord, endWord) in self.memo else 0



def test():
    data = [
        (('hit','cog',[]),0),
        (('hit','cog',['hot', 'cog']),0),
        (('hit','cog',['hot', 'cog', 'got']), 4),
        (('hit','cog',["hot","dot","dog","lot","log"]),0),
        (('hit','cog',["hot","dot","dog","lot","log","cog"]),5),
        (('hit','cog',["hot","dot","dog","lot","log","cog","hog"]), 4),
        (('abc','def',['abc','bcd','cdf','fde','def','dec','cfe']),4),
        (('abc','def',['abc','ace','cfe','efd']),0),
        (('abc','def',['abc','def','ace','cfe']),4),
        (('abc','def',['abc','abe','abd','cfe', 'cde', 'feb', 'fae', 'fac', 'def']),4),
        (("leet","code",["lest","leet","lose","code","lode","robe","lost"]),5)
    ]
    s = Solution()
    #test_fixture(s.ladderLength1, data)
    test_fixture(s.ladderLength_spf, data)

test()
