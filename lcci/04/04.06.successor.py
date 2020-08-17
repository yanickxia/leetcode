class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root:
            return None
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        node = self.inorderSuccessor(root.left, p)
        if node:
            return node
        return root


if __name__ == '__main__':
    s = Solution()
    print(s.inorderSuccessor(TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(1)))
