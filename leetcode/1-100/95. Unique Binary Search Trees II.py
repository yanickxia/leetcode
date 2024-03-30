# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.gen([i for i in range(1, n + 1)])

    def gen(self, nums: List[int]) -> List[TreeNode]:
        rs = []
        if not nums:
            return [None]

        for n in nums:
            less = [x for x in nums if x < n]
            bigger = [x for x in nums if x > n]

            ll = self.gen(less)
            rr = self.gen(bigger)
            for l in ll:
                for r in rr:
                    root = TreeNode(n)
                    root.left = l
                    root.right = r
                    rs.append(root)
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.generateTrees(3))
