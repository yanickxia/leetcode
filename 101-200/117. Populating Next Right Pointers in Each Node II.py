"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        rs = {}
        self.__connect(root, 0, rs)
        for i in range(99999):
            if i not in rs:
                break
            row = rs[i]
            for i in range(len(row) - 1):
                row[i].next = rs[i + 1]

        return root

    def __connect(self, root: Node, level, rs):
        if not root:
            return

        self.__connect(root.left, level + 1, rs)
        self.__connect(root.right, level + 1, rs)

        if level not in rs:
            rs[level] = []

        rs[level].append(root)

        return


if __name__ == '__main__':
    s = Solution()
    x = s.connect(Node(1, Node(2, Node(4), Node(5)), Node(3, right=Node(7))))
    print(x)
