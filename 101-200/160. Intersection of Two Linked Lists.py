# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            if pa != None:
                pa = pa.next
            else:
                pa = headB
            if pb != None:
                pb = pb.next
            else:
                pb = headA
        return pa
