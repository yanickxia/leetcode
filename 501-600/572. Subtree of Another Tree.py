# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False

        def is_same(a: TreeNode, b: TreeNode):
            if not a and not b:
                return True

            if a and b and a.val == b.val:
                return is_same(a.left, b.left) and is_same(a.right, b.right)
            return False

        return is_same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


if __name__ == '__main__':
    s = Solution()
    print(s.isSubtree(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)),
                      TreeNode(4, TreeNode(1), TreeNode(2))))
