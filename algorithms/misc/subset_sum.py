import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, len(args[0]), kw, te-ts)
        return result

    return timed

def _get_memo_key(target, start):
    return "{}/{}".format(target, start)


def _get_subset_sum(arr, target, start, memo):
    if _get_memo_key(target, start) in memo:
        return memo[_get_memo_key(target, start)]
    if target == 0:
        return True
    if start == len(arr):
        return False
    take = _get_subset_sum(arr, target - arr[start], start+1, memo)
    no_take =_get_subset_sum(arr, target, start+1, memo)
    memo[_get_memo_key(target-arr[start], start)] = take
    memo[_get_memo_key(target, start)] = no_take
    return take or no_take

@timeit
def get_subset_sum(arr, target):
    memo = {}
    return _get_subset_sum(arr, target, 0, memo)

class TestSubsetSum(object):
    def test_subset_sum(self):
        assert get_subset_sum([19, 3, 7, 10, 11], 18)
        assert not get_subset_sum([19, 3, 7, 10, 11], 8)
        assert get_subset_sum([16, 8, 10, 4, 24], 18)
        assert not get_subset_sum([16, 8, 10, 4, 24], 19)
        assert get_subset_sum([17, 4, 19, -6, 1], -2)
        assert get_subset_sum([1, 1, 1, 1, 1, 1, 1], 7)
        assert not get_subset_sum([x for x in range(100)], 1000000)