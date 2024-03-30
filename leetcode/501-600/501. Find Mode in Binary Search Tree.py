# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 20Min
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def __findMore(root: TreeNode, counter):
            if not root:
                return
            if root.val not in counter:
                counter[root.val] = 1
            else:
                counter[root.val] += 1

            __findMore(root.left, counter)
            __findMore(root.right, counter)

        rs = {}
        __findMore(root, rs)

        c = collections.Counter(rs).most_common(1)

        ans = []
        for key in rs:
            if rs[key] == c[0][1]:
                ans.append(key)

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMode(TreeNode(1, TreeNode(1), TreeNode(2))))
    print(s.findMode(TreeNode(1, None, TreeNode(2))))
    print(s.findMode(TreeNode(2147483647)))
    print(s.findMode(TreeNode(1, right=TreeNode(2, TreeNode(2)))))
