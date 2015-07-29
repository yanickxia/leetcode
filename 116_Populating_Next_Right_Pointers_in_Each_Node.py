__author__ = 'Yann'


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root: TreeLinkNode):
        if root == None:
            return

        while root != None:
            self.__connect_one_node__(root)
            root = root.left

    def __connect_one_node__(self, node: TreeLinkNode):
        if node.left == None:
            return

        while node != None:
            node.left.next = node.right
            if node.next != None:
                node.right.next = node.next.left
            node = node.next



s = Solution()
n1 = TreeLinkNode(1)
n2 = TreeLinkNode(2)
n3 = TreeLinkNode(3)
n1.left = n2
n1.right = n3

s.connect(n1)
