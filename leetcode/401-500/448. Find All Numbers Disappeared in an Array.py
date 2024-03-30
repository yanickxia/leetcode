class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        a_array = [1] + [0] * (len(nums))
        for x in nums:
            a_array[x] = 1

        rs = []
        for i in range(0, len(a_array)):
            if a_array[i] == 0:
                rs.append(i)

        return rs


s = Solution()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
