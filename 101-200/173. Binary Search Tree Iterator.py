# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = collections.deque()
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        n = self.stack.pop()
        ret = n.val

        if n.right:
            n = n.right
            while n:
                self.stack.append(n)
                n = n.left

        return ret

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == '__main__':
    root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))

    obj = BSTIterator(root)

    print(obj.next())
    print(obj.next())
    print(obj.next())
    print(obj.next())
    print(obj.next())
    print(obj.next())
    print(obj.next())
    print(obj.next())
