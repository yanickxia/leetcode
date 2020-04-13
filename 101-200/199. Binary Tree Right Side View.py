# Definition for a binary tree node.
from typing import List


###
### Linked: https://leetcode.com/problems/binary-tree-right-side-view/
###
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        result = {0: [root.val]}
        self.level_travel(root, result, 1)

        keys = list(result.keys())
        keys.sort()

        ints = []
        for i in keys:
            ints.append(result[i][-1])

        return ints

    def level_travel(self, root: TreeNode, result: dict, level: int):
        if root is None:
            return
        if root.left is not None:
            if level not in result:
                result[level] = [root.left.val]
            else:
                result[level].append(root.left.val)
            self.level_travel(root.left, result, level + 1)
        if root.right is not None:
            if level not in result:
                result[level] = [root.right.val]
            else:
                result[level].append(root.right.val)
            self.level_travel(root.right, result, level + 1)


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.right = n5
    n3.right = n4

    s = Solution()
    s.rightSideView(n1)
