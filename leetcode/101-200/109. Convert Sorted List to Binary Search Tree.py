# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        index_cache = {}

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if head.next is None:
            return TreeNode(head.val)

        i = 0
        root = head
        while root:
            i += 1
            root = root.next

        mid = int(i / 2)
        i = 0
        root = head
        lend = None
        rbegin = None
        while i != mid - 1:
            root = root.next
            i += 1
        lend = root

        rbegin = root.next.next

        x = TreeNode(root.next.val)
        lend.next = None
        ll = self.sortedListToBST(head)
        rr = self.sortedListToBST(rbegin)

        x.left = ll
        x.right = rr
        return x


if __name__ == '__main__':
    s = Solution()
    x= s.sortedListToBST(ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9))))))
    print(x)
