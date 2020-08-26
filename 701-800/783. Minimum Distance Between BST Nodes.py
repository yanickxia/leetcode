# LINK 530

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def travel(root, nodes):
            if not root:
                return
            nodes.append(root.val)
            travel(root.left, nodes)
            travel(root.right, nodes)

        nodes = []
        travel(root, nodes)
        nodes = sorted(nodes)

        for i in range(len(nodes) - 1):
            nodes[i] = abs(nodes[i] - nodes[i + 1])

        return min(nodes)