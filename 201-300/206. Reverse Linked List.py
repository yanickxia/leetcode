# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list_node = None
        if head is not None:
            new_list_node = ListNode(head.val)
        else:
            return new_list_node

        while head.next is not None:
            head = head.next
            temp = ListNode(head.val)
            temp.next = new_list_node
            new_list_node = temp

        return new_list_node
