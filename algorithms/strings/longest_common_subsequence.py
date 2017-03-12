
# def _get_string_from_matrix(s, substr, matrix, row, col):
#     if matrix[row][col] == 0:
#         return substr
#     if matrix[row - 1][col] >= matrix[row][col - 1]: # left
#         return _get_string_from_matrix(s, substr, matrix, row - 1, col)
#     elif matrix[row][col - 1] > matrix[row - 1][col]: # up
#         return _get_string_from_matrix(s, substr, matrix, row, col - 1)
#     else: # matrix[row - 1][col - 1] == matrix[row][col] - 1: # diagonal
#         return _get_string_from_matrix(s, substr + s[col-1], matrix, row - 1, col - 1)

# def get_string_from_matrix(matrix, str_1):
#     reversed_output = _get_string_from_matrix(str_1, '', matrix, len(matrix) - 1, len(matrix[0]) - 1)
#     return ''.join(reversed(reversed_output))

def longest_common_subsequence_dp(str_1, str_2):
    rows = len(str_2) + 1
    cols = len(str_1) + 1
    matrix = []
    for x in range(rows): matrix.append([0] * cols)
    for row in range(1, rows):
        for col in range(1, cols):
            if str_2[row-1] == str_1[col-1]:
                matrix[row][col] = matrix[row-1][col-1] + 1
            else:
                matrix[row][col] = max(matrix[row-1][col], matrix[row][col-1])
    return matrix[rows-1][cols-1]

def longest_common_subsequence_dp_no_bt(str_1, str_2):
    cols = len(str_1) + 1
    matrix = []
    for x in range(2): matrix.append([0] * cols)
    print matrix
    for row in range(1, len(str_2)+1):
        for col in range(1, cols):
            if str_2[row-1] == str_1[col-1]:
                matrix[1][col] = matrix[0][col-1] + 1
            else:
                matrix[1][col] = max(matrix[0][col], matrix[1][col-1])
        if row != len(str_2):
            matrix[0] = matrix[1]
            matrix[1] = [0] * cols
    return matrix[1][cols-1]


class Solution(object):
    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)

class TestLongestCommonSubsequence(object):
    def test_longest_common_subsequence(self):
        assert longest_common_subsequence_dp("abcdaf", "acbcf") == 4
        assert longest_common_subsequence_dp("abc", "def") == 0
        assert longest_common_subsequence_dp("a", "abcdefghi") == 1
        assert longest_common_subsequence_dp("abcdefghi", "a") == 1
        assert longest_common_subsequence_dp("", "") == 0
        assert longest_common_subsequence_dp("a", "") == 0
        assert longest_common_subsequence_dp("", "a") == 0

    def test_leet_code_solutions(self):
        s = Solution()
        assert s.isSubsequence("abc", "ahbgdc")
        assert not s.isSubsequence("axc", "ahbgdc")