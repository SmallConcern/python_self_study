class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_lowest_common_ancestor(root, num1, num2):
    if not root or root.val == num1 or root.val == num2:
        return root
    r = find_lowest_common_ancestor(root.left, num1, num2)
    r2 = find_lowest_common_ancestor(root.right, num1, num2)
    if r and not r2: return r
    elif r2 and not r: return r2
    elif r and r2:
        return root
    else:
        return None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return find_lowest_common_ancestor(root, p.val, q.val)

class TestLeetcodeQuestion(object):
    def test_leetcode_question(self):
        root = TreeNode(3, left=TreeNode(5), right=TreeNode(1))
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2, left=TreeNode(7), right=TreeNode(4))
        root.right.right = TreeNode(8)
        root.right.left = TreeNode(0)
        s = Solution()
        assert s.lowestCommonAncestor(root, TreeNode(1), TreeNode(2)).val == 3

class TestLowestCommonAncestor(object):
    def test_lowest_common_ancestor(self):
        """
        Tree looks like this:
             3
           /   \
          6     8
         / \     \
        2   11    13
            /\    /
           9  5  7

        """
        root = TreeNode(3, left=TreeNode(6), right=TreeNode(8))
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(11, left=TreeNode(9), right=TreeNode(5))
        root.right.right = TreeNode(13, left=TreeNode(7))
        assert find_lowest_common_ancestor(root, 2, 5).val == 6
        assert find_lowest_common_ancestor(root, 8, 11).val == 3
        assert find_lowest_common_ancestor(root, 3, 7).val == 3
        assert find_lowest_common_ancestor(root, 2, 6).val == 6
        assert find_lowest_common_ancestor(root, 3, 9).val == 3

