from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        rs = self.__levelOrderBottom(root)
        rs.reverse()
        return rs

    def __levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ll = self.__levelOrderBottom(root.left)
        rr = self.__levelOrderBottom(root.right)

        rs = []
        cur = [[root.val]]

        for i in range(max(len(ll), len(rr))):
            if i < len(ll) and i < len(rr):
                ll[i].extend(rr[i])
                rs.append(ll[i])
            elif i < len(ll):
                rs.append(ll[i])
            elif i < len(rr):
                rs.append(rr[i])
        rs = cur + rs

        return rs


if __name__ == '__main__':
    s = Solution()
    x = s.levelOrderBottom(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    print(x)
