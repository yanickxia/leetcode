# You are given the heads of two sorted linked lists list1 and list2.
#
#  Merge the two lists into one sorted list. The list should be made by
# splicing together the nodes of the first two lists.
#
#  Return the head of the merged linked list.
#
#
#  Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
#  Example 2:
#
#
# Input: list1 = [], list2 = []
# Output: []
#
#
#  Example 3:
#
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
#
#  Constraints:
#
#
#  The number of nodes in both lists is in the range [0, 50].
#  -100 <= Node.val <= 100
#  Both list1 and list2 are sorted in non-decreasing order.
#
#
#  Related Topics Linked List Recursion 👍 22193 👎 2174


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.

from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        l1_head = list1
        l2_head = list2

        root = ListNode(0, None)
        tail = root

        while l1_head is not None and l2_head is not None:
            if l1_head.val < l2_head.val:
                tail.next = ListNode(l1_head.val)
                l1_head = l1_head.next
            else:
                tail.next = ListNode(l2_head.val)
                l2_head = l2_head.next
            tail = tail.next

        while l1_head is not None:
            tail.next = ListNode(l1_head.val)
            l1_head = l1_head.next
            tail = tail.next

        while l2_head is not None:
            tail.next = ListNode(l2_head.val)
            l2_head = l2_head.next
            tail = tail.next

        return root.next


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists(None, None))
