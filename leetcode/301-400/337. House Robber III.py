# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cache = {}

    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root in self.cache:
            return self.cache[root]

        val = root.val
        ll = self.rob(root.left.left) if root.left is not None else 0
        lr = self.rob(root.left.right) if root.left is not None else 0
        rl = self.rob(root.right.left) if root.right is not None else 0
        rr = self.rob(root.right.right) if root.right is not None else 0

        self.cache[root] = max(val + ll + lr + rl + rr, self.rob(root.left) + self.rob(root.right))
        return self.cache[root]


if __name__ == '__main__':
    s = Solution()

    t2 = TreeNode(2)
    t1 = TreeNode(1, right=t2)
    t4 = TreeNode(4)
    t3 = TreeNode(3, t1, t4)

    print(s.rob(t3))
