
class AlienAlphabet(object):
    def __init__(self, words):
        self.alien_words = words
        self.relationships = self._get_letter_relationships()
        self.alphabet = self._get_alphabet()

    def _get_letter_relationships(self):
        if len(self.alien_words) < 2:
            return []
        relationships = set()
        for i in range(0, len(self.alien_words)-1):
            word_1 = self.alien_words[i]
            word_2 = self.alien_words[i+1]
            for j in range(min(len(word_1),len(word_2))):
                if word_1[j] != word_2[j]:
                    relationship = (word_1[j], word_2[j])
                    if relationship not in relationships:
                        relationships.add((word_1[j], word_2[j]))
                    break
        return relationships

    def _get_alphabet(self):
        graph = {}
        letters = set([char for word in self.alien_words for char in word ])
        for letter in letters:
            graph[letter] = []
        for relation in self.relationships:
            graph[relation[1]].append(relation[0])
        order = []
        while len(order) < len(letters):
            next_letters = [l for l in graph if len(graph[l]) == 0]
            # cycle, no info for some letter, or mult. solution
            if len(next_letters) != 1:
                return None
            next_letter = next_letters.pop()
            order.append(next_letter)
            # remove vertex and all its edges
            del graph[next_letter]
            for letter in graph:
                graph[letter] = [edge for edge in graph[letter] if edge != next_letter]
        return "".join(order)



class TestAlienAlphabet():
    def test_alien_alphabet(self):
        dict = ["bcca", "babc", "dacd", "aad", "aac"]
        aa = AlienAlphabet(dict)
        print aa.relationships
        print aa.alphabet