# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:

        t1_root = self.__find(t1, t2.val)

        if not t1_root:
            return False

        t1 = t1_root

        return self.__eq_tree(t1,t2)

    def __find(self, t: TreeNode, val) -> TreeNode:
        if t.val == val:
            return t

        if t.left:
            left = self.__find(t.left, val)
            if left:
                return left

        if t.right:
            right = self.__find(t.right, val)
            if right:
                return right

    def __eq_tree(self,  t1: TreeNode, t2: TreeNode):
        if t1.val != t2.val:
            return False

        left = True if not t1.left and not t2.left else False
        if t1.left and t2.left:
            left = self.__eq_tree(t1.left, t2.left)
        right = True if not t1.right and not t2.right else False
        if t2.right and t1.right:
            right = self.__eq_tree(t1.right, t2.right)

        return left and right

if __name__ == '__main__':
    s = Solution()
    print(s.checkSubTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(2)))