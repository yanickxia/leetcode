# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        if k == 0:
            return head

        size = 1
        root = head
        while root.next is not None:
            root = root.next
            size += 1

        k %= size
        if k == 0:
            return head

        k = size - k
        root = head
        for i in range(k - 1):
            root = root.next

        lend = root
        rbegin = root.next

        while root.next is not None:
            root = root.next

        root.next = head
        lend.next = None

        return rbegin


if __name__ == '__main__':
    s = Solution()
    print(s.rotateRight(ListNode(1), 1))
    print(s.rotateRight(ListNode(0, ListNode(1, ListNode(2))), 4))
    print(s.rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))
