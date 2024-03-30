from typing import List


# Given nums = [1,1,1,2,2,3]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1: return N
        left, right = 0, 1
        while right < N:
            while right < N and nums[right] == nums[left]:
                right += 1
            left += 1
            if right < N:
                nums[left] = nums[right]
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
    # print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    # print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
    # print(s.removeDuplicates([]))
