import random

def quick_sort(items):
    if len(items) > 1:
        pivot_index = len(items) /2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)
        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items
    return items

def test_quick_sort_simple():
    random_arr = [random.randint(-50,100) for x in range(20)]
    assert random_arr != sorted(random_arr)
    assert quick_sort(random_arr) == sorted(random_arr)
