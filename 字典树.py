class Node:
    def __init__(self):
        self.data={}
        self.is_word=False
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,word):
        node=self.root
        for char in word:
            child=node.data.get(char)
            if child is None:
                node.data[char]=Node()
            node=node.data[char]
        node.is_word=True
