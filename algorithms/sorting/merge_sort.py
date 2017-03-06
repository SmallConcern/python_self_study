
import sys

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)/2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        left_arr.append(sys.maxint)
        right_arr.append(sys.maxint)
        while i < len(arr):
            arr[i] = min([left_arr[0], right_arr[0]])
            if arr[i] == left_arr[0]:
                left_arr.pop(0)
            elif arr[i] == right_arr[0]:
                right_arr.pop(0)
            i += 1
    return arr

def gen_random_array(size, max_val):
    import random
    return [random.randint(-max_val, max_val) for x in xrange(size)]

def test_random_sort():
    arr = gen_random_array(100,1000)
    assert arr != sorted(arr)
    assert merge_sort(arr) == sorted(arr)