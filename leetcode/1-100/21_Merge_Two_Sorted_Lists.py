# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        self.root = None

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l3 = None

        if l1 is None and l2 is None:
            return self.root

        if l1 is None:
            while l2 is not None:
                l3 = self.append(l3, ListNode(l2.val))
                l2 = l2.next
            return self.root

        if l2 is None:
            while l1 is not None:
                l3 = self.append(l3, ListNode(l1.val))
                l1 = l1.next
            return self.root

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                l3 = self.append(l3, ListNode(l1.val))
                l1 = l1.next
            else:
                l3 = self.append(l3, ListNode(l2.val))
                l2 = l2.next

        while l1 is not None:
            l3 = self.append(l3, ListNode(l1.val))
            l1 = l1.next

        while l2 is not None:
            l3 = self.append(l3, ListNode(l2.val))
            l2 = l2.next

        return self.root

    def append(self, l3, node):
        if l3 is None:
            l3 = node
            self.root = l3
        else:
            l3.next = node
            l3 = l3.next
        return l3


s = Solution()
l1 = None
l2 = ListNode(0)

s.mergeTwoLists(l1, l2)
