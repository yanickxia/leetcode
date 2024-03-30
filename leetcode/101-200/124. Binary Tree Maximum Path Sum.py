# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cache = {}

    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return float('-INF')

        def dfs(node: TreeNode):
            if not node:
                return 0
            if node in self.cache:
                return self.cache[node]

            rs = max(node.val + dfs(node.left), node.val + dfs(node.right), node.val)
            self.cache[node] = rs
            return rs

        cur = root.val
        l = dfs(root.left)
        r = dfs(root.right)
        if l > 0:
            cur += l
        if r > 0:
            cur += r

        return max(cur,
                   self.maxPathSum(root.left),
                   self.maxPathSum(root.right))


if __name__ == '__main__':
    s = Solution()

    print(s.maxPathSum(TreeNode(9, TreeNode(6), TreeNode(-3, TreeNode(-6), TreeNode(2, TreeNode(2, TreeNode(-6,
                                                                                                            TreeNode(
                                                                                                                -6)),
                                                                                                TreeNode(-6)))))))
    print(s.maxPathSum(TreeNode(1, TreeNode(-2), TreeNode(3))))
    print(s.maxPathSum(TreeNode(2, TreeNode(-1))) == 2)
    print(s.maxPathSum(TreeNode(5, TreeNode(4), TreeNode(8))) == 17)
    s = Solution()
    print(s.maxPathSum(TreeNode(0)) == 0)
    s = Solution()
    print(s.maxPathSum(TreeNode(-10, TreeNode(35), TreeNode(7))) == 35)
    s = Solution()
    print(s.maxPathSum(
        TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))) == 3)
    s = Solution()

    s = Solution()
    print(s.maxPathSum(TreeNode(1, TreeNode(2))) == 3)
    s = Solution()
    print(s.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15, TreeNode(7))))))
    s = Solution()
    print(s.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6)
    s = Solution()
    print(s.maxPathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                                TreeNode(8, TreeNode(13), TreeNode(4, right=TreeNode(1))))))
