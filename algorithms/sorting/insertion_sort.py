def swap(arr, swap_1, swap_2):
    temp = arr[swap_1]
    arr[swap_1] = arr[swap_2]
    arr[swap_2] = temp

def insertion_sort(arr):
    if len(arr) > 1:
        for x in range(1, len(arr)):
            swap_index = x
            while swap_index > 0 and arr[swap_index] < arr[swap_index-1]:
                swap(arr, swap_index, swap_index-1)
                swap_index -= 1
    return arr

def gen_random_array(size, max_val):
    import random
    return [random.randint(-max_val, max_val) for x in xrange(size)]

def test_random_sort():
    arr = gen_random_array(100,1000)
    assert arr != sorted(arr)
    assert insertion_sort(arr) == sorted(arr)