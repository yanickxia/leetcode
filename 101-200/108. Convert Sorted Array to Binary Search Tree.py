# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])


        mid = int(len(nums)/2)
        less = nums[0:mid]
        right = nums[mid+1:]

        root = TreeNode(nums[mid])

        left = self.sortedArrayToBST(less)
        right = self.sortedArrayToBST(right)
        root.left = left
        root.right = right
        return root
if __name__ == '__main__':
    s = Solution()
    x= s.sortedArrayToBST([-10,-3,0,5,9])
    print(x)