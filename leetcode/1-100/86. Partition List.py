# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_node = None
        bigger_node = None
        less_root_node = None
        right_root_node = None
        if head is None:
            return None

        while head is not None:
            current_x = head.val
            if current_x < x:
                if less_node is None:
                    less_node = head
                    less_root_node = less_node
                else:
                    less_node.next = head
                    less_node = less_node.next
            else:
                if bigger_node is None:
                    bigger_node = head
                    right_root_node = bigger_node
                else:
                    bigger_node.next = head
                    bigger_node = bigger_node.next
            head = head.next

        if bigger_node is not None:
            bigger_node.next = None
        if less_root_node is None:
            return right_root_node

        less_node.next = right_root_node
        return less_root_node


n1 = ListNode(1)
n2 = ListNode(4)
n1.next = n2
n3 = ListNode(3)
n2.next = n3
n4 = ListNode(2)
n3.next = n4
n5 = ListNode(5)
n4.next = n5
n6 = ListNode(2)
n5.next = n6

s = Solution()

nn1 = ListNode(1)

print(s.partition(nn1, 0))
print(s.partition(n1, 3))
