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

# 5Min
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def isPath(h:ListNode, n:TreeNode):
            if not h:
                return True
            if not n or h.val != n.val:
                return False
            else:
                return isPath(h.next, n.left) or isPath(h.next, n.right)

        if not root:
            return False
        if not head:
            return True
        if head.val == root.val:
             if isPath(head, root):
                 return True
             else:
                 return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        else:
            return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
