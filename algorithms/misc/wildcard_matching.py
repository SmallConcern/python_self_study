from __future__ import print_function

def wildcard_matching(input_str, pattern):
    pattern = ' ' + pattern
    input_str = ' ' + input_str
    rows = len(input_str)
    cols = len(pattern)
    matrix = []
    for x in range(rows): matrix.append([True] + [False] * cols)
    for row in range(rows):
        for col in range(cols):
            if pattern[col] == '?' or pattern[col] == input_str[row]:
                if row > 0:
                    matrix[row][col] = matrix[row - 1][col - 1] | matrix[row][col]
            elif pattern[col] == '*':
                matrix[row][col] = matrix[row-1][col] | matrix[row][col-1]
            else:
                matrix[row][col] = 0
    return matrix[rows-1][cols-1]


class Solution(object):
    def isMatch(self, s, p):
        return bool(wildcard_matching(s, p))

class TestWildcardMatching(object):
    def print_truth_matrix(self, matrix):
        print('')
        for row in matrix:
            for value in row:
                    print("{} ".format(bool(value)), end='')
            print('')

    def test_wild_card_matching(self):
        assert wildcard_matching("xaylmz", "x?y*z")

    def test_leetcode_tests(self):
        s = Solution()
        assert not s.isMatch("aa", "a")
        assert s.isMatch("aa", "aa")
        assert not s.isMatch("aaa", "aa")
        assert s.isMatch("aa", "*")
        assert s.isMatch("aa", "a*")
        assert s.isMatch("ab", "?*")
        assert not s.isMatch("aab", "c*a*b")
        assert not s.isMatch("", "?")