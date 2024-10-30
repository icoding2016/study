"""
1647. Minimum Deletions to Make Character Frequencies Unique
Medium
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string.
For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

 

Constraints:

    1 <= s.length <= 105
    s contains only lowercase English letters.



"""

from collections import Counter, defaultdict


class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        num_chr = defaultdict(list)
        for k, c in counter.items():
            num_chr[c].append(k)
        used_cnt = list(num_chr.keys())
        del_count = 0
        for n, cs in num_chr.items():
            if len(cs) > 1:
                for i in range(len(cs) - 1):
                    x = n
                    while x > 0:
                        x -= 1
                        del_count += 1
                        if x not in used_cnt:
                            used_cnt.append(x)
                            break
        return del_count
