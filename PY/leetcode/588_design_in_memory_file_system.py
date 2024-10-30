"""
588. Design In-Memory File System
https://leetcode.com/problems/design-in-memory-file-system/description/
https://leetcode.ca/all/588.html

Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. 
    If it is a file path, return a list that only contains this file's name. 
    If it is a directory path, return the list of file and directory names in this directory.
    Your output (file and directory names together) should in lexicographic order.
mkdir: Given a directory path that does not exist, you should make a new directory according to the path.
    If the middle directories in the path don't exist either, you should create them as well.
    This function has void return type.
addContentToFile: Given a file path and file content in string format.
    If the file doesn't exist, you need to create that file containing given content.
    If the file already exists, you need to append given content to original content.
    This function has void return type.
readContentFromFile: Given a file path, return its content in string format.


Example:
Input:
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]

Explanation:
filesystem

 

Note:
    You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
    You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
    You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.


"""


class FSNode():
    valid_ftype = ['D', 'F']
    def __init__(self, name:str, ftype:str):
        self.name = name
        assert ftype.upper() in self.valid_ftype
        self.ftype = ftype.upper()
        self.content = ''
        self.children = None
        if self.ftype == 'D':
            self.children = {}

    def ls(self):
        if self.ftype == 'F':
            return [self.name,]
        return [node.name for node in self.children]

    def find_child(self, name:str) -> 'FSNode':
        if self.ftype == 'F':
            # raise ValueError(f'File type of node does not support find_child method.')
            return None
        if name in self.children:
            return self.children[name]
        return None

    def add_child(self, node:'FSNode'):
        assert node, f'Null FSNode'
        assert self.ftype == 'D', f'File type does not support add_child'
        if self.find_child(node.name):
            raise ValueError(f'the node with the same name already exists.')
        self.children[node.name] = node
        snames = sorted(self.children.keys())
        nodes = {k:self.children[k] for k in snames}
        self.children = nodes


class FS():
    def __init__(self):
        self.root = FSNode('/', 'D')

    def find(self, pth:str) -> FSNode:
        if not pth:
            return None
        if pth == '/':
            return self.root
        pnames = pth.split('/')
        root = self.root
        node = None
        while pnames:
            name, pnames = pnames[0], pnames[1:] 
            node = root.find_child(name)
            root = node
        return node

    def ls(self, pth:str) -> list:
        if not pth:
            return []
        if pth == '/':
            return self.root.ls()
        node = self.find(pth)
        if node:
            return node.ls()
        return []


    def mkdir(self, pth:str):
        names = pth.split('/')
        root = self.root
        for i, name in enumerate(names):
            node = root.find_child(name)
            if not node:
                node = FSNode(name, ftype='D')
                root.add_child(node)
            root = node

    def addContentToFile(self, pth:str, content:str):
        node = self.find(base)
        if node:
            node.content += content
            return

        names = pth.split('/')
        base, fn = '/'.join(names[:-2]), names[-1]
        if not base:
            node = self.root
        else:
            self.mkdir(base)
            node = self.find(base)
        node.content += content

    def readContentFromFile(self, pth:str) -> str:
        node = self.find(pth)
        if not node:
            raise ValueError(f'File not found')
        return node.content
