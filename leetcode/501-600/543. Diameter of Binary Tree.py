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
        self.ans = 0

        def longest(node: TreeNode):
            if not node:
                return -1

            l = longest(node.left) + 1
            r = longest(node.right) + 1
            self.ans = max(l + r, self.ans)
            return max(l, r)

        longest(root)
        return self.ans


if __name__ == '__main__':
    s = Solution()
    print(s.diameterOfBinaryTree(TreeNode(1)))
    print(s.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))
