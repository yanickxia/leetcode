# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        cur = None
        if t1 and t2:
            cur = TreeNode(t1.val + t2.val)
            cur.left = self.mergeTrees(t1.left, t2.left)
            cur.right = self.mergeTrees(t1.right, t2.right)
        elif t1:
            cur = TreeNode(t1.val)
            cur.left = self.mergeTrees(t1.left, None)
            cur.right = self.mergeTrees(t1.right, None)
        elif t2:
            cur = TreeNode(t2.val)
            cur.left = self.mergeTrees(t2.left, None)
            cur.right = self.mergeTrees(t2.right, None)
        return cur
