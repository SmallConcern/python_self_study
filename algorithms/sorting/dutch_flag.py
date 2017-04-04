def dutch_flag_sort(arr, mid):
    i = 0
    j = 0
    n = len(arr)-1

    while j <= n:
        if arr[j] < mid:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > mid:
            arr[j], arr[n] = arr[n], arr[j]
            n -= 1
        else:
            j += 1
        print arr


def counting_sort(arr):
    from collections import Counter
    c = Counter(arr)
    start = 0
    for key in sorted(c.keys()):
        arr[start:start+c[key]] = [key] * c[key]
        start += c[key]


class TestDutchFlagSort(object):
    @staticmethod
    def gen_dutch_flag(size):
        import random
        return [random.randint(0, 2) for _ in range(size)]

    def test_dutch_flag_sort(self):
        arr = [2, 1, 2, 0, 1, 0, 2, 1, 2]
        dutch_flag_sort(arr, 1)
        assert arr == [0, 0, 1, 1, 1, 2, 2, 2, 2]

    def test_dutch_flag_counting_sort(self):
        arr = [2, 1, 2, 0, 1, 0, 2, 1, 2]
        counting_sort(arr)
        assert arr == [0, 0, 1, 1, 1, 2, 2, 2, 2]

    def test_large_inputs(self):
        arr = TestDutchFlagSort.gen_dutch_flag(1000000)
        arr2 = sorted(arr)
        counting_sort(arr, 1)
        assert arr == arr2