# Definition for singly-linked list.
import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        eof = False

        while not eof:
            if head.next is None:
                eof = True
                break

            next_node = head.next
            if next_node is None:
                head.next = ListNode(val=head.val)

            else:
                v = math.gcd(next_node.val, head.val)
                head.next = ListNode(val=v, next=next_node)

            head = head.next.next

        return root


def listToListNode(lst) -> ListNode:
    root = ListNode(lst[0])
    head = root
    for i in range(1, len(lst)):
        head.next = ListNode(lst[i])
        head = head.next
    return root


def listNodeToList(lst: ListNode):
    arr = []
    while lst is not None:
        arr.append(lst.val)
        lst = lst.next
    return arr


if __name__ == '__main__':
    s = Solution()
    print(listNodeToList(s.insertGreatestCommonDivisors(listToListNode([3]))))
    print(listNodeToList(s.insertGreatestCommonDivisors(listToListNode([18, 6, 10, 3]))))
