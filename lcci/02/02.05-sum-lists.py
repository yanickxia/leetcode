# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ro1 = l1
        ro2 = l2
        carry = False
        i, j = 0, 0
        while l1 or l2:
            if l1 and l2:
                v = l1.val + l2.val + (1 if carry else 0)
                if v >= 10:
                    carry = True
                else:
                    carry = False
                l1.val = v % 10
                l2.val = v % 10

                l1 = l1.next
                l2 = l2.next

            elif l1:
                i += 1
                v = l1.val + (1 if carry else 0)
                if v >= 10:
                    carry = True
                else:
                    carry = False
                l1.val = v % 10
                l1 = l1.next
            else:
                j += 1
                v = l2.val + (1 if carry else 0)
                if v >= 10:
                    carry = True
                else:
                    carry = False
                l2.val = v % 10
                l2 = l2.next

        if i >= j:
            if carry:
                last = ListNode(1)
                head = ro1
                while head.next:
                    head = head.next
                head.next = last
                return ro1

            else:
                return ro1
        else:
            if carry:
                last = ListNode(1)
                head = ro2
                while head.next:
                    head = head.next
                head.next = last
                return ro2
            else:
                return ro2


if __name__ == '__main__':
    s = Solution()
    print(s.addTwoNumbers(ListNode(5), ListNode(5)))
    print(s.addTwoNumbers(ListNode(7, ListNode(1, ListNode(6))), ListNode(5, ListNode(9, ListNode(2)))))
