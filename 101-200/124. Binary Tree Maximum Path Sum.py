# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.cache = {}
        self.maxium = float("-INF")

    def maxPathSum(self, root: TreeNode) -> int:
        self.__maxPathSum(root)
        return self.maxium

    def __maxPathSum(self, root) -> int:
        if not root:
            return float("-INF")

        if root in self.cache:
            return self.cache[root]

        if not root.left and not root.right:
            self.cache[root] = root.val
            return root.val

        cur = root.val
        if root.left:
            l = self.__maxPathSum(root.left)
            if l > 0:
                cur += l
        if root.right:
            r = self.__maxPathSum(root.right)
            if r > 0:
                cur += r

        m = max(cur, self.__maxPathSum(root.left), self.__maxPathSum(root.right))
        if m > self.maxium:
            self.maxium = m
        return cur


if __name__ == '__main__':
    s = Solution()
    print(s.maxPathSum(TreeNode(5, TreeNode(4,), TreeNode(8))))

    s = Solution()
    print(s.maxPathSum(TreeNode(0)))
    s = Solution()
    print(s.maxPathSum(TreeNode(-10, TreeNode(35), TreeNode(7))) == 35)
    s = Solution()
    print(s.maxPathSum(
        TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))) == 3)
    s = Solution()
    print(s.maxPathSum(TreeNode(2, TreeNode(-1))) == 2)
    s = Solution()
    print(s.maxPathSum(TreeNode(1, TreeNode(2))) == 3)
    s = Solution()
    print(s.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15, TreeNode(7))))))
    s = Solution()
    print(s.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6)
