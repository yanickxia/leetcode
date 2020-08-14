# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 2min
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        link_len = 0
        root = head
        while head:
            link_len += 1
            head = head.next

        jump = link_len - k
        head = root
        while jump > 0:
            jump -= 1
            head = head.next
        return head.val
