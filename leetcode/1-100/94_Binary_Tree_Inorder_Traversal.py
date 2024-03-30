__author__ = 'Yann'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        node = root
        solution = []
        while node!= None or len(stack)>0:
            if node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                solution.append(node.val)
                node = node.right
        return solution


n1 = TreeNode(1)
n2 = TreeNode(2)
n1.left = n2

s = Solution()
print(s.inorderTraversal(n1))
