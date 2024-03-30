# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        nums = self.__sumNumbers(root)

        if not nums:
            return 0
        return sum([int(''.join(x)) for x in nums])

    def __sumNumbers(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return None

        rs = []

        if root.left:
            ll = self.__sumNumbers(root.left)
            rs.extend(ll)
        if root.right:
            rr = self.__sumNumbers(root.right)
            rs.extend(rr)

        if not rs:
            return [[str(root.val)]]

        return [[str(root.val)] + x for x in rs]


if __name__ == '__main__':
    s = Solution()
    print(s.sumNumbers(None))
    print(s.sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))
