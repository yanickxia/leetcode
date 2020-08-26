# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 17 Min
class Solution:
    def __init__(self):
        self.cache = {}

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def travel(node: TreeNode):
            if not node:
                return 0

            if node in self.cache:
                return self.cache[node]

            rs = node.val + travel(node.left) + travel(node.right)

            self.cache[node] = rs
            return rs

        def __findFrequentTreeSum(node: TreeNode, counter):
            if not node:
                return
            rs = travel(node)
            if rs not in counter:
                counter[rs] = 1
            else:
                counter[rs] += 1

            __findFrequentTreeSum(node.left, counter)
            __findFrequentTreeSum(node.right, counter)

        counter = {}
        __findFrequentTreeSum(root, counter)
        maxum = collections.Counter(counter).most_common(1)[0][1]
        ans = []
        for key in counter:
            if counter[key] == maxum:
                ans.append(key)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findFrequentTreeSum(None))
    print(s.findFrequentTreeSum(TreeNode(5, TreeNode(2), TreeNode(-3))))
    print(s.findFrequentTreeSum(TreeNode(5, TreeNode(2), TreeNode(-5))))
