"""

208. Implement Trie (Prefix Tree)
Medium
https://leetcode.com/problems/implement-trie-prefix-tree/description/

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

 
Constraints:
    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 104 calls in total will be made to insert, search, and startsWith.

"""


class TrieNode:
    def __init__(self, val=""):
        self.val = val
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if not word:
            return
        node = self.root
        for i, ch in enumerate(word):
            if ch not in node.children:
                new_node = TrieNode(ch)
                node.children[ch] = new_node
                node = new_node
            else:
                node = node.children[ch]
        node.end_of_word = True
        return

    def walk(self, word: str) -> "TrieNode":
        if not word:
            return None
        node = self.root
        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self.walk(word)
        if not node:
            return False
        return node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.walk(prefix)
        if not node:
            return False
        return True
