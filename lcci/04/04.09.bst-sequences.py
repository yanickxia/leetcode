# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        res = []

        if root is None: return [[]]
        temp = [root.val]

        def help(root, queue, path):
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
            if len(queue) == 0:
                res.append(temp + path)
            for i, next_root in enumerate(queue):
                next_queue = queue[:i] + queue[i + 1:]
                help(next_root, next_queue, path + [next_root.val])

        help(root, [], [])
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.BSTSequences(TreeNode(5, TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3))))))
    print(s.BSTSequences(TreeNode(1, right=TreeNode(2))))
    print(s.BSTSequences(TreeNode(3, TreeNode(5), TreeNode(1))))
