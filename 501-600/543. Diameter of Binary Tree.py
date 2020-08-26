# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        def longest(node: TreeNode):
            if not node:
                return 0
            if node.left and node.right:
                return max(longest(node.left), longest(node.right)) + 1
            if node.left:
                return longest(node.left) + 1
            if node.right:
                return longest(node.right) + 1
            return 0

        if root.left and root.right:
            return max(longest(root.left) + longest(root.right) + 2, self.diameterOfBinaryTree(root.left),
                       self.diameterOfBinaryTree(root.right))
        if root.left:
            return max(longest(root.left) + 1, self.diameterOfBinaryTree(root.left))
        if root.right:
            return max(longest(root.right) + 1, self.diameterOfBinaryTree(root.right))
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.diameterOfBinaryTree(TreeNode(1)))
    print(s.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))
