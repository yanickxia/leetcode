class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0:
            return []

        a_array = [0] * (len(nums) + 1)
        rs = []
        for n in nums:
            if a_array[n] == 0:
                a_array[n] = 1
            else:
                rs.append(n)

        return rs


s = Solution()
print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
