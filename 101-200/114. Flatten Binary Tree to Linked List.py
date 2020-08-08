# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return
        ll, llend = None,None
        if root.left:
            ll = self.flatten(root.left)
            llend = ll
            while llend.right:
                llend = llend.right
        rr = None
        if root.right:
            rr = self.flatten(root.right)

        if llend is not None:
            llend.right = rr

        if ll is not None:
            root.right = ll
        else:
            root.right = rr

        root.left = None


        return root

if __name__ == '__main__':
    s = Solution()
    x = s.flatten(TreeNode(1, TreeNode(2, TreeNode(3),TreeNode(4)), TreeNode(5,None, TreeNode(6))))
    print(x)