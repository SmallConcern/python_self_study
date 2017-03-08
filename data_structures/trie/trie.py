from collections import defaultdict


class TrieNode(object):
    def __init__(self, char='', terminus=False):
        self.char = char
        self.children = defaultdict(TrieNode)
        self.terminus = terminus

    def add_child(self, trie_node):
        self.children[trie_node.char] = trie_node


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.add_child(new_node)
                node = new_node
        node.terminus = True

    def is_prefix(self, word):
        return self.is_word(word, True)

    def is_word(self, word, prefix=False):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.terminus if not prefix else True