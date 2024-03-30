# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rs = {}
        self.level_order(root, rs, 0)
        as_rs = []
        for v in rs.itervalues():
            as_rs.append(v)

        return as_rs

    def level_order(self, root, rs, level):
        if root is None:
            return
        if rs.get(level) is None:
            rs[level] = []
            rs[level].append(root.val)
        else:
            rs[level].append(root.val)

        if root.left is not None:
            self.level_order(root.left, rs, level + 1)
        if root.right is not None:
            self.level_order(root.right, rs, level + 1)

    def printLevelOrder(self,root):
        if root is None:
            return

        # Create an empty queue for level order traversal
        queue = []

        # Enqueue Root and initialize height
        queue.append(root)

        while (len(queue) > 0):
            # Print front of queue and remove it from queue
            print queue[0].val,
            node = queue.pop(0)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)


t1 = TreeNode(0)
t2 = TreeNode(-1)
t3 = TreeNode(15)

t1.left = t2
t1.right = t3

s = Solution()
print(s.levelOrder(t1))

print(s.printLevelOrder(t1))
