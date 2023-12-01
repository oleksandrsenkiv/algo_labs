
class Node:
    def __init__(self):
        self.is_end_of_string = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def add_pattern(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end_of_string = True

    def find_word(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return node.is_end_of_string
        return node.is_end_of_string

    def find_prefix(self, pref):
        node = self.root
        for char in pref:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def create_trie(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.add_pattern(pattern)
    return trie
