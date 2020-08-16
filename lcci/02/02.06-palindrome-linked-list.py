class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        pre = slow
        curr = slow

        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        slow.next = None

        while pre and head:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(ListNode(1,ListNode(2,ListNode(3, ListNode(2,ListNode(1)))))))
    print(s.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
