class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        ta, tb = headA, headB
        while ta != tb:
            ta = ta.next if ta else headB
            tb = tb.next if tb else headA
        return tb