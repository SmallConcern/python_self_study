import pytest
import random

class InvalidNumberSet(Exception):
    pass


def mean(num_set):
    if not num_set:
        raise InvalidNumberSet("Must provide data set to mean function.")
    return sum(num_set)/float(len(num_set))

def mode(num_set):
    pass

def median_simple(num_set):
    if len(num_set) % 2 == 0:
        idx = len(num_set)/2
        return sum(sorted(num_set)[idx-1:idx+1])/float(2)
    else:
        return sorted(num_set)[len(num_set)/2]

def _median_helper(num_set, target_idx):
    partition = random.choice(num_set)
    smaller, larger = [], []
    pivot_count = 0
    for num in num_set:
        if num < num_set[target_idx]:
            smaller.append(num)
        elif num == partition:
            pivot_count += 1
        else:
            larger.append(num)
    if len(smaller) > target_idx:
        return _median_helper(smaller, target_idx)
    elif len(smaller) + pivot_count > target_idx:
        return partition
    else:
        return _median_helper(larger, target_idx - len(smaller) - pivot_count)

def median(num_set):
    if not num_set:
        raise InvalidNumberSet("Must provide valid data set to median function.")
    idx = len(num_set)/2
    return _median_helper(num_set, idx)



class TestMmm(object):
    def test_mean(self):
        assert mean([10, 20, 30]) == 20.0
        assert mean([2]) == 2.0
        assert mean([3, 4]) == 3.5
        with pytest.raises(InvalidNumberSet):
            mean([])

    def test_median(self):
        assert median_simple([]) == 0
        assert median_simple([2, 5, 7, 7, 9]) == 7
        assert median_simple([11, 7, 18, 4]) == float(11+7)/2
        with pytest.raises(InvalidNumberSet):
            median([]) == 0
        assert median([2, 5, 7, 7, 9]) == 7
        assert median([11, 7, 18, 4]) == float(11 + 7) / 2