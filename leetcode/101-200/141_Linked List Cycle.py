__author__ = 'Yann'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head:ListNode):
        if head == None:
            return False
        head.val = None
        while head.next != None:
            head = head.next
            if head.val == None:
                return True
            head.val = None

        return False
