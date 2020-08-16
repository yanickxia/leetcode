# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head

        apper_set = {head.val}
        pre = head
        root = head
        while root:
            if root.val not in apper_set:
                apper_set.add(root.val)
                pre.next = root
                pre = root
                root = root.next
                pre.next = None
            else:
                root = root.next
        return head

if __name__ == '__main__':
    s = Solution()
    x = s.removeDuplicateNodes(ListNode(1, ListNode(2, ListNode(3, ListNode(2)))))
    print(x)