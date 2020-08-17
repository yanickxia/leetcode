# Definition for a binary tree node.
from typing import List

# 00:08:07

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        nodes = []
        self.__listOfDepth(tree,0,nodes)
        return nodes

    def __listOfDepth(self, tree: TreeNode, level, nodes: List[ListNode]):

        if level >= len(nodes):
            nodes.append(ListNode(tree.val))
        else:
            curr = nodes[level]
            while curr.next:
                curr = curr.next
            curr.next = ListNode(tree.val)

        if tree.left:
            self.__listOfDepth(tree.left, level+1, nodes)
        if tree.right
            self.__listOfDepth(tree.right, level+1, nodes)
