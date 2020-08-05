# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        lst = self.inorder(root)

        return lst[k-1]

    def inorder(self, root: TreeNode):
        if root.left is None and root.right is None:
            return [root.val]
        left, right = [], []
        if root.left is not None:
            left = self.inorder(root.left)
        if root.right is not None:
            right = self.inorder(root.right)

        return left + [root.val] + right


if __name__ == '__main__':
    s = Solution()

    t2 = TreeNode(2)
    t1 = TreeNode(1, right=t2)
    t4 = TreeNode(4)
    t3 = TreeNode(3, t1, t4)

    print(s.kthSmallest(t3, 1))
