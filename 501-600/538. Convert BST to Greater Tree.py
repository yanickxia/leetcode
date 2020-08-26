# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 14 Min
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.__convertBST(root, 0)
        return root

    def __convertBST(self, root: TreeNode, ext):
        if not root:
            return None

        def sum(node: TreeNode) -> int:
            if not node:
                return 0
            return node.val + sum(node.left) + sum(node.right)

        r = sum(root.right)
        self.__convertBST(root.left, root.val + r + ext)
        self.__convertBST(root.right, ext)

        root.val += r + ext


if __name__ == '__main__':
    s = Solution()

    x = s.convertBST(TreeNode(2, TreeNode(0, TreeNode(-4), TreeNode(1)), TreeNode(3)))
    print(x)
