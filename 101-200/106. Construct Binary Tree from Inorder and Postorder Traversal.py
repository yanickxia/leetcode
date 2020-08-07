# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        left_in = inorder[0:i]
        right_in = inorder[i + 1:]

        left_post = postorder[0:len(left_in)]
        right_post = postorder[len(left_in):len(postorder) - 1]

        l = self.buildTree(left_in, left_post)
        r = self.buildTree(right_in, right_post)

        root.left = l
        root.right = r

        return root


if __name__ == '__main__':
    s = Solution()
    # n = s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    n =s.buildTree([2,3,1],[3,2,1])
    #n = s.buildTree([1, 2], [2, 1])
    print(n)
