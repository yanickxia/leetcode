__author__ = 'Yann.Xia'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root:TreeNode, p:TreeNode, q:TreeNode):
        l_paths = self.findNode(root, p, [])
        r_paths = self.findNode(root, q, [])

        l_paths.reverse()

        for x in l_paths:
            if x in r_paths:
                return x.val

    def findNode(self, root:TreeNode, node:TreeNode, paths:list):
        paths.append(root)

        if node.val > root.val:
            self.findNode(root.right, node, paths)
        elif node.val < root.val:
            self.findNode(root.left, node, paths)

        return paths


s = Solution()

t1 = TreeNode(6)
t2 = TreeNode(2)
t3 = TreeNode(8)

t1.left = t2
t1.right = t3

print(s.lowestCommonAncestor(t1, t1, t2))
