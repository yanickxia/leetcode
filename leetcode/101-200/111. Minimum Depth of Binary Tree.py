# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0


        ll = 9999999
        if root.left is not None:
            ll = self.minDepth(root.left) + 1

        rr =9999999999
        if root.right is not None:
            rr = self.minDepth(root.right) + 1

        if root.right is None and root.left is None:
            return 1

        return min(ll, rr)

if __name__ == '__main__':
    s = Solution()
    print(s.minDepth(TreeNode(1, None, TreeNode(2))))
    # x = s.minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    # print(x)