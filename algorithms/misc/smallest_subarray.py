import sys


def find_smallest_sub_array(arr, sub_array):
    dp = []
    for _ in sub_array:
        dp.append([-1] * (len(arr) + 1))
    for row in xrange(len(sub_array)):
        for col in xrange(len(arr)-1, -1, -1):
            if arr[col] == sub_array[row]:
                dp[row][col] = col
            else:
                dp[row][col] = dp[row][col+1]
    min_distance = sys.maxint
    min_pair = None
    for col in range(len(arr)):
        sub_array_indexes = []
        answer = True
        for row in range(len(sub_array)):
            if dp[row][col] == -1:
                answer = False
                break
            sub_array_indexes.append(dp[row][col])
        if answer:
            max_distance = max(sub_array_indexes)
            if (max_distance - col) < min_distance:
                min_distance = max_distance - col
                min_pair = (col, max_distance)
    return min_pair


class TestSmallestSubarray(object):
    def test_smallest_subarray(self):
        sub_array = [1, 5, 9]
        #      0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
        arr = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
        assert find_smallest_sub_array(arr, sub_array) == (7, 10)