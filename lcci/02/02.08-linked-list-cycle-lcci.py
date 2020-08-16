class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 快慢指针, 数学证明懒得背

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast != slow: # 这个叛逆必须加 因为上面循环跳出也可能是循环体结束了导致的
            return
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow