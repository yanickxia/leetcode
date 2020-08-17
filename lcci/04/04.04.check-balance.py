# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        return abs(self.__depth(root.left) - self.__depth(root.right)) <= 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def __depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.__depth(root.left), self.__depth(root.right)) + 1