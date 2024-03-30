# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 12 Min
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        val = 0
        if root.left:
            if not root.left.left and not root.left.right:
                val += root.left.val
            else:
                val += self.sumOfLeftLeaves(root.left)
        if root.right:
            val += self.sumOfLeftLeaves(root.right)

        return val


if __name__ == '__main__':
    s = Solution()
    print(s.sumOfLeftLeaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
