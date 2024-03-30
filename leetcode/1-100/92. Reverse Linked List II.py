# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        if m == n:
            return head

        i = 1
        root = head
        m_node, before_m_node, n_node, after_n_node, tmp_last_header, tmp_header = None, None, None, None, None, None
        while root:
            if i == m - 1:
                before_m_node = root
            elif i == m:
                tmp_header = root
                tmp_last_header = root

            elif m < i <= n:
                tmp = root
                root = root.next
                tmp.next = tmp_header
                tmp_header = tmp
                i += 1
                continue
            elif i == n + 1:
                after_n_node = root
                root = root.next
                tmp_last_header.next = after_n_node
                i += 1
                continue

            root = root.next
            i += 1

        if after_n_node is None:
            tmp_last_header.next = None

        if before_m_node is not None:
            before_m_node.next = tmp_header
        else:
            return tmp_header


        return head


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBetween(ListNode(3, ListNode(5)), 1, 2))
    print(s.reverseBetween(ListNode(5), 1, 1))
    print(s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4))
