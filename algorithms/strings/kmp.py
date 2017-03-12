

class KMP(object):
    def __init__(self):
        pass

    def generate_prefix_array(self, pattern):
        prefix_array = [0] * len(pattern)
        j, i = 0, 1
        while i < len(pattern):
            if pattern[i] == pattern[j]:
                prefix_array[i] = j + 1
                j += 1
                i += 1
            else:
                if j != 0:
                    j = prefix_array[j - 1]
                else:
                    prefix_array[i] = 0
                    i += 1
        return prefix_array

    def substring_search(self, pattern, search_string):
        if pattern == search_string or len(pattern) == 0:
            return 0
        if len(pattern) > len(search_string):
            return -1
        prefix_array = self.generate_prefix_array(pattern)
        search_idx, pattern_idx = 0, 0
        while (search_idx < len(search_string) and pattern_idx < len(pattern)):
            if search_string[search_idx] == pattern[pattern_idx]:
                search_idx += 1
                pattern_idx += 1
            else:
                if pattern_idx != 0:
                    pattern_idx = prefix_array[pattern_idx - 1]
                else:
                    search_idx += 1
        if pattern_idx == len(pattern):
            return search_idx - len(pattern)
        return -1

class Solution(object):
    def strStr(self, haystack, needle):
        kmp = KMP()
        return kmp.substring_search(needle, haystack)


class TestKMP(object):
    def test_kmp_prefix_array(self):
        kmp = KMP()
        text = "abcxabcdabcdabcy"
        pattern = "abcdabcy"
        assert kmp.substring_search(pattern, text) == 8
        assert kmp.substring_search("a", "a") == 0
        assert kmp.substring_search("abc", "a") == -1
        assert kmp.substring_search("ab", "cab") == 1
        assert kmp.substring_search("", "") == 0
        assert kmp.substring_search("", "foo") == 0
        assert kmp.substring_search("f", "") == - 1
