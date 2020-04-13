# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        g = set(G)
        count = 0
        flag = False
        while head is not None:
            if head.val in g:
                flag = True
            if head.val not in g and flag:
                count += 1
                flag = False
            head = head.next
        if flag:
            count += 1
        return count


if __name__ == '__main__':
    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)

    n0.next = n1
    n1.next = n2
    n2.next = n3

    print(Solution().numComponents(n0, [0, 1, 3]))

    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n3.next = n4
    n4.next = n0
    n0.next = n2
    n2.next = n1
    print(Solution().numComponents(n3, [4]))
