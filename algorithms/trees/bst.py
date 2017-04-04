
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    @staticmethod
    def in_order(node):
        if node:
            BinarySearchTree.in_order(node.left)
            print(node.val)
            BinarySearchTree.in_order(node.right)

    @staticmethod
    def pre_order(node):
        if node:
            print(node.val)
            BinarySearchTree.pre_order(node.left)
            BinarySearchTree.pre_order(node.right)

    @staticmethod
    def post_order(node):
        if node:
            BinarySearchTree.post_order(node.left)
            BinarySearchTree.post_order(node.right)
            print(node.val)

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

def test_traversals():
    tn = TreeNode(50, left=TreeNode(25), right=TreeNode(75))
    tn.left.left = TreeNode(15, left=TreeNode(10), right=TreeNode(20))
    tn.left.right = TreeNode(35, left=TreeNode(30), right=TreeNode(40))
    tn.right.right = TreeNode(90, left=TreeNode(85), right=TreeNode(100))
    tn.right.left = TreeNode(65, left=TreeNode(55), right=TreeNode(70))
    print ("PRE: \n")
    BinarySearchTree.pre_order(tn)
    print ("IN: \n")
    BinarySearchTree.in_order(tn)
    print ("POST: \n")
    BinarySearchTree.post_order(tn)


def test_bst_empty_init():
    bst = BinarySearchTree()
    assert bst != None
    assert not bst.root
    assert len(bst) == 0
    assert bst.size == 0