from collections import namedtuple

import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print '%r %2.2f sec' % \
              (method.__name__, te-ts)
        return result
    return timed


class KnapsackItem(namedtuple('KnapsackItem', ['weight', 'value'])):
    __slots__ = ()

def _get_knapsack_value_r(items, max_weight, value, index):
    if max_weight < 0:
        return 0
    if max_weight == 0 or index >= len(items):
        return value
    return max(_get_knapsack_value_r(items, max_weight - items[index].weight, value + items[index].value, index + 1),
               _get_knapsack_value_r(items, max_weight, value, index + 1))

@timeit
def get_knapsack_value_r(items, max_weight):
    return _get_knapsack_value_r(list(reversed(sorted(items))), max_weight, 0, 0)

def _get_knapsack_value_memo(items, max_weight, value, index, memo):
    # we don't appear to hit this, maybe my data sets don't support memoization or this
    # doesn't work like I think it does
    if "{}-{}".format(max_weight, index) in memo:
        return memo["{}-{}".format(max_weight, index)]
    if max_weight < 0:
        return 0
    if max_weight == 0 or index >= len(items):
        return value
    knap_value =  max(_get_knapsack_value_r(items, max_weight - items[index].weight, value + items[index].value, index + 1),
                      _get_knapsack_value_r(items, max_weight, value, index + 1))
    memo["{}-{}".format(max_weight, index)] = knap_value
    return knap_value

@timeit
def get_knapsack_value_memo(items, max_weight):
    memo = {}
    return _get_knapsack_value_memo(list(reversed(sorted(items))), max_weight, 0, 0, memo)

@timeit
def get_knapsack_value_dp(items, max_weight):
    rows = len(items)
    cols = max_weight + 1
    matrix = []
    for x in range(rows): matrix.append([0] * cols)
    for row in range(0, rows):
        for col in range(1, cols):
            if items[row].weight <= col:
                matrix[row][col] = max(items[row].value + matrix[row-1][col - items[row].weight], matrix[row-1][col])
            else:
                matrix[row][col] = matrix[row-1][col]
    return matrix[rows-1][cols-1]


class TestKnapsackProblem(object):
    def gen_items(self, arr):
        items = []
        for item in arr:
            items.append(KnapsackItem(weight=item[0], value=item[1]))
        return items

    def gen_giant_input(self, size=10000):
        items = []
        l = range(size)
        for first, second in zip(l, l[1:]):
            items.append(KnapsackItem(weight=first, value=second))
        return items

    def test_knapsack_problem_recursive(self):
        assert get_knapsack_value_r(self.gen_items([[1, 1], [3, 4], [4, 5], [5, 7]]), 7) == 9
        assert get_knapsack_value_r(self.gen_items([[4, 5], [1, 8], [2, 4], [3, 0], [2, 5], [2, 3]]), 5) == 17
        assert get_knapsack_value_r(self.gen_items([[23, 92], [31, 57], [29, 49], [44, 68], [53, 60], [38, 43],
                                                    [63,67], [85,84], [89,87], [82,72]]), 165) == 309
        size = 150 # blows stack at 1000
        print get_knapsack_value_r(self.gen_giant_input(size), size/2)

    def test_knapsack_problem_memo(self):
        assert get_knapsack_value_memo(self.gen_items([[1, 1], [3, 4], [4, 5], [5, 7]]), 7) == 9
        assert get_knapsack_value_memo(self.gen_items([[4, 5], [1, 8], [2, 4], [3, 0], [2, 5], [2, 3]]), 5) == 17
        assert get_knapsack_value_memo(self.gen_items([[23, 92], [31, 57], [29, 49], [44, 68], [53, 60], [38, 43],
                                                     [63, 67], [85, 84], [89, 87], [82, 72]]), 165) == 309
        size = 150  # blows stack at 1000
        print get_knapsack_value_memo(self.gen_giant_input(size), size / 2)

    def test_knapsack_problem_dp(self):
        assert get_knapsack_value_dp(self.gen_items([[1,1], [3,4], [4,5], [5,7]]), 7) == 9
        assert get_knapsack_value_dp(self.gen_items([[4,5], [1,8], [2,4], [3,0], [2,5], [2,3]]), 5) == 17
        assert get_knapsack_value_dp(self.gen_items([[23,92],[31,57],[29,49],[44,68],[53,60],[38,43],
                                                                   [63,67],[85,84],[89,87],[82,72]]), 165) == 309
        size = 1000 # mem error at 100000, does size 10,000 (5,000 knapsack items, 5,000 weight) in 21.22s (value: 5099)
        print get_knapsack_value_dp(self.gen_giant_input(size), size / 2)
