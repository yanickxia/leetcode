# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        nodeList = []
        while head.next is not None:
            nodeList.append(head)
            head = head.next
        nodeList.append(head)

        del nodeList[-n]

        if len(nodeList) == 0:
            return None
        if len(nodeList) == 1:
            nodeList[0].next = None
            return nodeList[0]

        for i in range(0, len(nodeList) - 1):
            nodeList[i].next = nodeList[i + 1]
        nodeList[-1].next = None

        return nodeList[0]


s = Solution()

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3

head = s.removeNthFromEnd(l1, 1)

print head
