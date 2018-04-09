# -*- coding:utf-8 -*-

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        return self.clone_graph(node, {})

    def clone_graph(self, node, cp):
        print(node.label)
        root_node = UndirectedGraphNode(node.label)
        if len(node.neighbors) == 0:
            cp[node.label] = root_node
            return root_node

        neighbors = []
        for child in node.neighbors:
            if cp.get(child.label) is not None:
                neighbors.append(cp[child.label])
            elif child.label == node.label:
                neighbors.append(root_node)
            else:
                neighbors.append(self.clone_graph(child, cp))
        root_node.neighbors = neighbors
        cp[root_node.label] = root_node
        return root_node


s = Solution()

u0 = UndirectedGraphNode(0)
u1 = UndirectedGraphNode(1)
u2 = UndirectedGraphNode(2)
u3 = UndirectedGraphNode(3)

u0.neighbors = [u1, u2, u3]
u1.neighbors = [u2]
u2.neighbors = [u2]
u3.neighbors = [u1, u2, u3]

print(s.cloneGraph(u0))
