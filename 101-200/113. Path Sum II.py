from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        rs = []

        if root:
            self.p(root, sum, [], rs)
        return rs

    def p(self, root: TreeNode, sum, pre, rs):
        if not root.left and not root.right and sum == root.val:
            pre = pre.copy()
            pre.append(root.val)
            rs.append(pre)
            return
        if root.left:
            pre1 = pre.copy()
            pre1.append(root.val)
            self.p(root.left, sum - root.val, pre1, rs)
        if root.right:
            pre2 = pre.copy()
            pre2.append(root.val)
            self.p(root.right, sum - root.val, pre2, rs)


if __name__ == '__main__':
    s = Solution()
    print(s.pathSum(TreeNode(5,TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))), 22))