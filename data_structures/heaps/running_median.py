import heapq
import math

class RunningMedianFinder(object):
    def __init__(self, input_list):
        sorted_input = sorted(input_list)
        self.smallest_nums_max_heap = [-val for val in sorted_input[:len(sorted_input) / 2]]
        heapq.heapify(self.smallest_nums_max_heap)
        self.largest_nums_min_heap = sorted_input[len(sorted_input) / 2:]
        heapq.heapify(self.largest_nums_min_heap)

    def _balance_heaps(self):
        if len(self.smallest_nums_max_heap) - len(self.smallest_nums_max_heap) > 1:
            val = -heapq.heappop(self.smallest_nums_max_heap)
            heapq.heappush(self.largest_nums_min_heap, val)
        elif len(self.largest_nums_min_heap) - len(self.smallest_nums_max_heap) > 1:
            val = heapq.heappop(self.largest_nums_min_heap)
            heapq.heappush(self.smallest_nums_max_heap, val)

    def add_number(self, num):
        if num < -self.smallest_nums_max_heap[0]:
            heapq.heappush(self.smallest_nums_max_heap, -num)
        else:
            heapq.heappush(self.largest_nums_min_heap, num)
        self._balance_heaps()

    def get_median(self):
        if len(self.smallest_nums_max_heap) > len(self.largest_nums_min_heap):
            return -self.smallest_nums_max_heap[0]
        elif len(self.largest_nums_min_heap) > len(self.smallest_nums_max_heap):
            return self.largest_nums_min_heap[0]
        else:
            return (float(-self.smallest_nums_max_heap[0]) + float(self.largest_nums_min_heap[0])) / 2


def verify_heaps_balanced(median_finder):
    assert math.fabs(len(median_finder.smallest_nums_max_heap) - len(median_finder.largest_nums_min_heap)) < 2

class TestRunningMedianFinder(object):
    def test_running_median_finder_init(self):
        rmf = RunningMedianFinder([10,4,3,2,11,100,6,4,5])
        assert rmf.smallest_nums_max_heap[0] == -4
        assert rmf.largest_nums_min_heap[0] == 5
        assert verify_heaps_balanced(rmf)

    def test_running_median_finder_get_median_from_init(self):
        rmf = RunningMedianFinder([10,4,3,2,11,100,6,4,5])
        assert rmf.get_median() == 5.0
        rmf =  RunningMedianFinder([7,4,6,5])
        assert rmf.get_median() == 5.5

    def test_running_median_finder_get_median(self):
        rmf = RunningMedianFinder([10,4,3,2,11,100,6,4,5])
        assert rmf.get_median() == 5.0
        verify_heaps_balanced(rmf)
        rmf.add_number(-1)
        assert -rmf.smallest_nums_max_heap[len(rmf.smallest_nums_max_heap)-1] == -1
        verify_heaps_balanced(rmf)
        rmf.add_number(-5)
        verify_heaps_balanced(rmf)
        assert rmf.get_median() == 4
        rmf.add_number(200)
        assert rmf.get_median() == 4.5