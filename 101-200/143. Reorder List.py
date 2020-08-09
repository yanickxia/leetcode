# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return
        h = head
        queue = collections.deque()
        pre = None
        while head:
            queue.append(head)
            head = head.next
        while queue:
            left = queue.popleft()
            if not queue:
                left.next = None
                if pre:
                    pre.next = left
                return
            right = queue.pop()

            left.next = right
            right.next = None
            if pre:
                pre.next = left

            pre = right


if __name__ == '__main__':
    s = Solution()
    h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s.reorderList(h)
    print(h)
    h = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    s.reorderList(h)
    print(h)
