# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        str_head = []
        while head.next is not None:
            str_head.append(head.val)
            head = head.next
        str_head.append(head.val)

        return str_head[::-1] == str_head


l1 = ListNode('1')
l2 = ListNode('2')
l1.next = l2
l3 = ListNode('1')
l2.next = l3

s = Solution()
print(s.isPalindrome(l1))
