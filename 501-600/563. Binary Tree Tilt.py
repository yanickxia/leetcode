# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0

        def calc_sum(node: TreeNode):
            if not node:
                return 0

            cur = node.val
            if node.left:
                cur += calc_sum(node.left)
            if node.right:
                cur += calc_sum(node.right)
            return cur

        return abs(calc_sum(root.left) - calc_sum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)


if __name__ == '__main__':
    s = Solution()
    print(s.findTilt(TreeNode(1, TreeNode(2), TreeNode(3))))
