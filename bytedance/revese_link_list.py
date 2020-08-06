# 给定一个单链表的头节点 head,实现一个调整单链表的函数，\
# 使得每K个节点之间为一组进行逆序，并且从链表的尾部开始组起，
# 头部剩余节点数量不够一组的不需要逆序。（不能使用队列或者栈作为辅助）

class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def reverse(self, node, n):
        i = 0
        root = node
        while root:
            i += 1
            root = root.next

        leave = i % n

        root = node
        while leave > 1:
            root = root.next
            leave -= 1

        while root.next:
            pre = root
            root = root.next
            tmp_header = root
            list_n = n
            while list_n > 1:
                list_n -= 1
                next_node = root.next
                root.next = next_node.next
                next_node.next = tmp_header
                tmp_header = next_node
            pre.next = tmp_header

        return node







if __name__ == '__main__':
    s = Solution()
    print(s.reverse(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))),3))
