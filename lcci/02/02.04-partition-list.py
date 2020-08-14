# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p, q = head, head
        while q:
            if q.val < x:
                q.val, p.val = p.val, q.val
                p = p.next
            q = q.next
        return head


if __name__ == '__main__':
    s = Solution()
    # 3->5->8->5->10->2->1
    x = s.partition(ListNode(3, ListNode(5, ListNode(8, ListNode(5, ListNode(10, ListNode(2, ListNode(1))))))), 5)
    print(x)
