from string import ascii_lowercase
from collections import deque

def get_word_set_from_dict():
    words = set()
    with open('dictionary.txt', 'r') as dictionary:
        for word in dictionary.read().split('\n'):
            words.add(word.lower())
    return words


class WordChains(object):
    def __init__(self, word_set):
        self.word_set = word_set

    def find_neighbors(self, word):
        neighbors = set()
        for i in range(len(word)+1):
            for char in ascii_lowercase:
                if word[:i] + char + word[i:] in self.word_set:
                    neighbors.add(word[:i] + char + word[i:])
        for i in range(len(word)):
            for char in ascii_lowercase:
                if word[:i] + char + word[i+1:] in self.word_set:
                    neighbors.add(word[:i] + char + word[i+1:])
            if word[:i] + word[i+1:] in self.word_set:
                neighbors.add(word[:i] + word[i+1:])
        return neighbors

    def find_word_chain(self, start, end):
        word_stack = deque([start])
        backtrack = {start: None}
        while word_stack:
            word = word_stack.popleft()
            for neighbor in self.find_neighbors(word):
                if neighbor not in backtrack:
                    backtrack[neighbor] = word
                    word_stack.append(neighbor)
                if neighbor == end:
                    break
        if end in backtrack:
            chain = []
            current_word = end
            while current_word is not None:
                chain.append(current_word)
                current_word = backtrack[current_word]
            chain.reverse()
            return chain
        else:
            return None


class TestWordChains(object):
    def test_find_neighbors(self):
        wc = WordChains(get_word_set_from_dict())
        assert "food" and "floods" and "floor" and "blood" and "flood" in wc.find_neighbors("flood")
        assert "hit" and "sip" and not "flip" in wc.find_neighbors("hip")
        assert "i" and not "u" in wc.find_neighbors("a")

    def test_find_word_chain(self):
        wc = WordChains(get_word_set_from_dict())
        assert set.difference(set(["casey", "case", "pase", "pale", "spale", "spall", "small"]) -
                                set(wc.find_word_chain("casey", "small"))) == set()
