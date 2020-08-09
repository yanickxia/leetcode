# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        flag = True
        pre = None
        while head:
            if flag:
                pre = head
                head = head.next
            else:
                next = head

                pre_last = head
                last = head.next

                if not last:
                    break

                while last.next:
                    pre_last = last
                    last = last.next

                pre_last.next = None
                pre.next = last
                last.next = head
                head = last.next

            flag = not flag


if __name__ == '__main__':
    s = Solution()
    h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s.reorderList(h)
    h = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    s.reorderList(h)
    print(h)
