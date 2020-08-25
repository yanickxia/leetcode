# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, top):
            if not node or node.val != top:
                return 0
            return 1 + max(dfs(node.left, top), dfs(node.right, top))

        return max(dfs(root.left, root.val) + dfs(root.right, root.val), self.longestUnivaluePath(root.left),
                   self.longestUnivaluePath(root.right))


if __name__ == '__main__':
    s = Solution()
    print(s.longestUnivaluePath(
        TreeNode(1, right=TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, TreeNode(1))))))
    print(s.longestUnivaluePath(TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, TreeNode(5)))))
    print(s.longestUnivaluePath(
        TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, right=TreeNode(5)))))
