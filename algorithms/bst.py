
class BinarySearchTree(object):
	def __init__(self):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

class TreeNode(object):
	def __init__(self, val, left=None, right=None, parent=None):
		self.val = val
		self.left = left
		self.right = right
		self.parent = parent

	def is_leaf(self):
		return not self.left and not self.right

def test_tree_node_utils():
	tn = TreeNode(10)
	assert tn.is_leaf()
	tn = TreeNode(10, left=TreeNode(5))
	assert not tn.is_leaf()


def test_tree_node_init():
	tn = TreeNode(1)
	assert tn
	assert not tn.left
	assert not tn.right
	assert not tn.parent
	assert tn.val == 1
	tn = TreeNode(10, left=TreeNode(10), right=TreeNode(15), parent=TreeNode(20))
	assert tn.val == 10
	assert tn.left.val == 10 
	assert tn.right.val == 15
	assert tn.parent.val == 20

def test_bst_empty_init():
	bst = BinarySearchTree()
	assert bst != None
	assert not bst.root
	assert len(bst) == 0
	assert bst.size == 0