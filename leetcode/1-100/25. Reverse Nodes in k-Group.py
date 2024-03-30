# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        root, org, cn, pre_last = head, head, None, None
        n = k

        tail = head
        ln = 1
        while root:
            tmp = root
            while tmp:
                if ln == k:
                    lnk = ln
                    # revse from root
                    head = root
                    tail = root
                    while lnk > 1:
                        root = root.next
                        if not root:
                            break

                        tail.next = root.next
                        root.next = head
                        head = root
                        root = tail
                        tmp = tail
                        lnk -= 1
                    if pre_last:
                        pre_last.next = head
                    pre_last = tail
                    ln = 1

                    if not cn:
                        cn = head
                    break
                else:
                    tmp = tmp.next
                    ln += 1
            if not tmp:
                break
            root = tmp.next


        rs = cn if cn else org
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))
    print(s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3))
