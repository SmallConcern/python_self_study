from trie import TrieNode
from trie import Trie

class TestTrie(object):
    def test_trie_node(self):
        tn = TrieNode('c')
        assert tn.char == 'c'
        tn.add_child(TrieNode('a'))
        assert tn.children.has_key('a')
        assert tn.children['a'].char == 'a'
        tn.children['a'].add_child(TrieNode('t'))
        assert tn.children['a'].children.has_key('t')

    def test_trie_add_word(self):
        trie = Trie()
        for word in ["cat", "car", "cab", "foo", "foobar"]:
            trie.add_word(word)
        assert trie.root.children.has_key('c')
        assert trie.root.children.has_key('f')
        c_node = trie.root.children['c']
        assert c_node.children.has_key('a')
        assert c_node.children['a'].children.has_key('t')
        assert c_node.children['a'].children.has_key('r')
        assert c_node.children['a'].children.has_key('b')
        assert not c_node.children['a'].children.has_key('p')

    def test_trie_is_word(self):
        trie = Trie()
        for word in ["cat", "car", "cab", "foo", "foobar"]:
            trie.add_word(word)
        assert trie.is_word("cat")
        assert not trie.is_word("ca")
        assert not trie.is_word("cap")
        assert trie.is_word("foo")
        assert trie.is_word("foobar")
        assert not trie.is_word("foob")

    def test_trie_is_prefix(self):
        trie = Trie()
        for word in ["cat", "car", "cab", "foo", "foobar"]:
            trie.add_word(word)
        assert trie.is_prefix("ca")
        assert trie.is_prefix("cat")
        assert trie.is_prefix("foob")
        assert not trie.is_prefix("a")