__author__ = 'Yann'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root == None:
            return
        self.invertRoot(root)

        return root

    def invertRoot(self, node):
        if node == None:
            return

        left = node.left
        node.left = node.right
        node.right = left

        if node.left != None:
            self.invertRoot(node.left)
        if node.right != None:
            self.invertRoot(node.right)
