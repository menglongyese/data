class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False
    def __repr__(self):
        return f"TrieNone({self.data})"


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TrieNode()
            node = node.data[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if not node:
                return False
        return node.is_word

    def startswith(self, prefix):
        node = self.root
        for chars in prefix:
            node = node.data.get(chars)
            if not node:
                return False
        return True


if __name__ == '__main__':
    # p=TrieNode('clood')
    tr = Trie()
    tr.insert("clood")
    print(tr)
