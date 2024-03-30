# Definition for a binary tree node.
from typing import List

# 30 Min
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        cur = root

        def build_node(node: TreeNode, delete: List[int], breaking: List[TreeNode]) -> TreeNode:
            if not node:
                return None

            if node.val not in delete:
                ll = build_node(node.left, delete, breaking)
                rr = build_node(node.right, delete, breaking)
                node.left = ll
                node.right = rr
                return node
            else:
                if not node.left and not node.right:
                    return None
                breaking.append(node)
                return None

        breaking = []
        ans = []
        rs = build_node(root, to_delete, breaking)
        if rs:
            ans.append(rs)
        for break_node in breaking:
            ans.extend(self.delNodes(break_node.left, to_delete))
            ans.extend(self.delNodes(break_node.right, to_delete))

        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.delNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))), [3, 5])
    print(ans)
