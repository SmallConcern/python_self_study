# This is a work in progress. need to implement more methods and max heap version.

class BinHeap:
	def __init__(self):
		self.heap_list = [0]
		self.current_size = 0

	def perc_up(self, i):
		while i / 2 > 0:
			if self.heap_list[i] < self.heap_list[i/2]:
				tmp = self.heap_list[i/2]
				self.heap_list[i/2] = self.heap_list[i]
				self.heap_list[i] = tmp
			i = i / 2

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