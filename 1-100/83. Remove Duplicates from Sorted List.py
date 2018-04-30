# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        new_head = ListNode(head.val)
        new_head_root = new_head
        while head.next is not None:
            head = head.next
            if new_head.val == head.val:
                continue
            else:
                new_head.next = ListNode(head.val)
                new_head = new_head.next

        return new_head_root


# l5 = ListNode(3)
# l4 = ListNode(3)
# l4.next = l5
# l3 = ListNode(2)
# l3.next = l4
l2 = ListNode(1)
# l2.next = l3
l1 = ListNode(1)
l1.next = l2

s = Solution()
x = s.deleteDuplicates(l1)
print()