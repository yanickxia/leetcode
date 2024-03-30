# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 6 Min
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = collections.deque()
        queue.append((root, 0))
        ans = []

        while queue:
            cur = queue.popleft()
            node, level = cur[0], cur[1]
            if level >= len(ans):
                ans.append(node.val)
            elif node.val > ans[level]:
                ans[level] = node.val

            if node.left:
                queue.append((node.left, level + 1,))
            if node.right:
                queue.append((node.right, level + 1))

        return ans
