# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def find(node: TreeNode, is_left, level) -> (int, int):
            if not node:
                return None
            cur, l, r = None, None, None
            if is_left:
                cur = node.val
            if node.left:
                l = find(node.left, True, level + 1)
            if node.right:
                r = find(node.right, False, level + 1)
            if l and r:
                if l[0] > r[0]:
                    return l
                return r
            if l:
                return l
            if r:
                return r

            if cur is None:
                return None

            return [level, cur]

        return find(root, True, 0)[1]


if __name__ == '__main__':
    s = Solution()
    print(s.findBottomLeftValue(TreeNode(0, None, TreeNode(-1))))
    print(s.findBottomLeftValue(TreeNode(0)))
    print(s.findBottomLeftValue(TreeNode(2, TreeNode(1), TreeNode(3))))
    print(s.findBottomLeftValue(
        TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))))
