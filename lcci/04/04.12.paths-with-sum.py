# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.__pathSum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def __pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        count = 0
        if root.val == sum:
            count += 1

        count += self.__pathSum(root.left, sum - root.val, )
        count += self.__pathSum(root.right, sum - root.val)
    
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.pathSum(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5))))), 3))
