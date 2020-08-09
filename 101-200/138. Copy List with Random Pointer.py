"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        all_nodes = []
        root = head
        i = 0
        while root:
            node = Node(root.val)
            all_nodes.append((i, node, root))
            if len(all_nodes) > 0:
                all_nodes[-1][1].next = node
            root = root.next
            i += 1

        for x in all_nodes:
            if x[2].random:
                tmp = None
                for y in all_nodes:
                    if y[2] == x[2].random:
                        tmp = y[0]
                x[1].random = all_nodes[tmp][1]

        return all_nodes[0][1] if len(all_nodes) > 0 else None


if __name__ == '__main__':
    s = Solution()

    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    n4 = Node(10)
    n5 = Node(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n1

    print(s.copyRandomList(n1))
