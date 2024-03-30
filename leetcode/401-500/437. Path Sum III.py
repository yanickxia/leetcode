# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 5.30Min
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        return self.__pathSum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def __pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        rs = 0
        if root.val == sum:
            rs += 1

        return rs + self.__pathSum(root.left, sum - root.val) + self.__pathSum(root.right, sum - root.val)


if __name__ == '__main__':
    s = Solution()
    print(s.pathSum(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, right=TreeNode(1))),
                             TreeNode(-3, right=TreeNode(11))), 8))
