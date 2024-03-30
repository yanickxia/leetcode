class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in sorted(nums):
            result += [item + [num] for item in result]
        return result



s = Solution()
print(s.subsets([1, 2, 3]))
print(s.subsets([1, 2, 3,4]))
print(s.subsets([1]))
