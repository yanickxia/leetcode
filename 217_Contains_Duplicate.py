__author__ = 'Yann.Xia'


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if nums == None or len(nums) == 0:
            return False

        max_num = max(nums)
        ls = [0] * (max_num + 1)
        flag = False

        for n in nums:
            if ls[n] == 0:
                ls[n] = 1
            else:
                flag = True
                break

        return flag





s = Solution()
print(s.containsDuplicate([]))