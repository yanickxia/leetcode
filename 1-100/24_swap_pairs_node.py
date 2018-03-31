# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None:
            return head

        rs = head.next
        last_pre = None
        while head is not None and head.next is not None:
            # old
            fst = head
            sed = head.next
            source_next = head.next.next

            # new
            if last_pre is not None:
                last_pre.next = sed
            fst.next = source_next
            sed.next = fst
            last_pre = fst
            head = source_next
        return rs

    def print_list(self, head):
        while head is not None:
            print(head.val)
            head = head.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

s = Solution()

s.print_list(s.swapPairs(l1))
