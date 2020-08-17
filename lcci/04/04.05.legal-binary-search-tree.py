# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# 0:15:38
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.__isValidBST(root.left, [float('-inf'),root.val-1]) and self.__isValidBST(root.right, [root.val+1,float('inf')])

    def __isValidBST(self, root: TreeNode, range) -> bool:
        if not root:
            return True

        if not (range[0] <= root.val <= range[1]):
            return False

        return self.__isValidBST(root.left, [range[0], root.val-1]) and self.__isValidBST(root.right, [root.val+1, range[1]])


if __name__ == '__main__':
    s = Solution()
    print(s.isValidBST(TreeNode(1, TreeNode(1))))
    print(s.isValidBST(TreeNode(10, TreeNode(5), TreeNode(15))))
    print(s.isValidBST(TreeNode(-2147483648, None, TreeNode(2147483647))))