from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]


if __name__ == '__main__':
    s = Solution()
    rs = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(rs, 3)

    print(rs)
    rs = [-1,-100,3,99]

    s.rotate(rs,2)

    print(rs)
