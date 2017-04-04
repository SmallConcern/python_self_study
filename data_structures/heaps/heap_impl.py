# This is a work in progress. need to implement more methods and max heap version.

class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i / 2 > 0:
            if self.heap_list[i] < self.heap_list[i/2]:
                self.heap_list[i/2], self.heap_list[i] = self.heap_list[i], self.heap_list[i/2]
            i /= 2

    def perc_down(self, i):
        while i * 2 < self.current_size:
            min_child = self.min_child(i)
            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
            i = min_child

    def peak(self):
        return self.heap_list[1]

    def pop_min(self):
        min = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1
        self.perc_down(1)
        return min

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

def test_bin_heap_perc_up():
    bh = BinHeap()
    assert bh.heap_list == [0]
    bh.heap_list = [0,2,3,1]
    bh.perc_up(3)
    assert bh.heap_list == [0,1,3,2]

def test_bin_heap_perc_down():
    bh = BinHeap()
    assert bh.heap_list == [0]
    bh.heap_list = [0,3,2,1,4,5]
    bh.current_size = 5
    bh.perc_down(1)
    assert bh.heap_list == [0,1,2,3,4,5]

def test_min_bin_heap_insert():
    bh = BinHeap()
    assert bh.heap_list == [0]
    assert bh.current_size == 0
    bh.insert(5)
    assert bh.heap_list == [0,5]
    assert bh.current_size == 1
    bh.insert(10)
    assert bh.heap_list == [0, 5, 10]
    bh.insert(1)
    assert bh.heap_list == [0, 1, 10, 5]
    bh.insert(100)
    assert bh.heap_list == [0, 1, 10, 5, 100]
    bh.insert(4)
    assert bh.heap_list == [0, 1, 4, 5, 100, 10]
    assert bh.current_size == 5

def test_bin_heap_get_min():
    bh = BinHeap()
    bh.insert(5)
    bh.insert(100)
    bh.insert(1)
    bh.insert(45)
    bh.insert(99)
    bh.insert(-5)
    bh.insert(0)
    assert bh.peak() == -5
    assert bh.pop_min() == -5
    assert bh.peak() == 0
    assert bh.pop_min() == 0
    assert bh.peak() == 1
    assert bh.heap_list == [0, 1, 45, 5, 100, 99]
