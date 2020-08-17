# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# 0:19:41
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.continas(root, p, q)[1]

    @staticmethod
    def continas(root: TreeNode, p: TreeNode, q: TreeNode) -> (int, TreeNode):
        cons = 0
        if root.val == p.val:
            cons += 1
        elif root.val == q.val:
            cons += 2

        if root.left:
            c, t = Solution.continas(root.left, p, q)
            if t:
                return (3, t)

            cons += c
            if cons == 3:
                return (3, root)
        if root.right:
            c, t = Solution.continas(root.right, p, q)
            if t:
                return (3, t)
            cons += c
            if cons == 3:
                return (3, root)
        return (cons, None)

if __name__ == '__main__':
    s = Solution()
    print(s.lowestCommonAncestor(TreeNode(3, TreeNode(5), TreeNode(1)), TreeNode(1), TreeNode(5)))