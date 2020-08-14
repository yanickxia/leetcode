class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 8 Min
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pre = node
        while node.next:
            next = node.next
            node.val = next.val
            pre = node
            node = node.next
        pre.next = None
