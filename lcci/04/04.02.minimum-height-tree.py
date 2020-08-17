from typing import List

# 3min
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 0:
            return None
        else:
            mid = int(len(nums) / 2)
            curr = TreeNode(nums[mid])

            left =  nums[:mid]
            right = nums[mid+1:]

            curr.left = self.sortedArrayToBST(left)
            curr.right = self.sortedArrayToBST(right)
            return curr


if __name__ == '__main__':
    s = Solution()
    rs = s.sortedArrayToBST([-10,-3,0,5,9])
    print(rs)