import unittest


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         s = Solution()
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()
