# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 30Min
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def bfs(node: TreeNode):
            queue = collections.deque()
            queue.append((0, node))
            apper_set = set()
            ans = None

            while queue:
                cur = queue.popleft()
                cur_node = cur[1]
                level = cur[0]
                if level not in apper_set:
                    ans = cur_node.val
                    apper_set.add(level)

                if cur_node.left:
                    queue.append((level + 1, cur_node.left))
                if cur_node.right:
                    queue.append((level + 1, cur_node.right))
            return ans
        return bfs(root)

if __name__ == '__main__':
    s = Solution()
    print(s.findBottomLeftValue(TreeNode(0, None, TreeNode(-1))))
    print(s.findBottomLeftValue(TreeNode(0)))
    print(s.findBottomLeftValue(TreeNode(2, TreeNode(1), TreeNode(3))))
    print(s.findBottomLeftValue(
        TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))))
