# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 11Min
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]
        rs = []
        if root.left:
            l = self.binaryTreePaths(root.left)
            for i in range(len(l)):
                l[i] = str(root.val) + "->" + l[i]
            rs.extend(l)
        if root.right:
            r = self.binaryTreePaths(root.right)
            for i in range(len(r)):
                r[i] = str(root.val) + "->" + r[i]
            rs.extend(r)
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.binaryTreePaths(TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(3))))
