# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 4Min
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''

        if t.left and t.right:
            return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"
        if t.left:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        if t.right:
            return str(t.val) + "()(" + self.tree2str(t.right) + ")"
        return str(t.val)