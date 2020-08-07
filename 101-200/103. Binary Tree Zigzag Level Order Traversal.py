# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        rs = self.__zigzagLevelOrder(root)

        for i in range(len(rs)):
            if i % 2== 1:
                tmp = rs[i]
                tmp.reverse()
                rs[i] = tmp

        return rs
    def __zigzagLevelOrder(self,root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ll = self.__zigzagLevelOrder(root.left)
        rr = self.__zigzagLevelOrder(root.right)
        rs = [[root.val]]
        for i in range(max(len(ll), len(rr))):
            if i < len(ll) and i < len(rr):
                ll[i].extend(rr[i])
                rs.append(ll[i])
            elif i < len(ll):
                rs.append(ll[i])
            elif i < len(rr):
                rs.append(rr[i])
        return rs

if __name__ == '__main__':
    s = Solution()
    print(s.zigzagLevelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
