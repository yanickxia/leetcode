# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = head

        new_root = None
        new_root_last = None

        while root:
            r1 = root
            r1_val = root.val
            if root.next != None:
                r2 = root.next
                r2_val = root.next.val

                if r1_val != r2_val:
                    root = root.next
                    if new_root is None:
                        new_root = r1
                        new_root_last = r1
                    else:
                        new_root_last.next = r1
                        new_root_last = new_root_last.next

                else:
                    while root.val == r2_val:
                        root = root.next
                        if root is None:
                            if new_root is not None:
                                new_root_last.next = None
                                break
                            else:
                                break



            else:
                if new_root is None:
                    new_root = r1
                else:
                    new_root_last.next = r1
                root = root.next

        return new_root


if __name__ == '__main__':
    s = Solution()
    print(s.deleteDuplicates(ListNode(1, ListNode(1))))
    print(s.deleteDuplicates(ListNode(1, ListNode(2, ListNode(2)))))
    print(s.deleteDuplicates(ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4)))))))
