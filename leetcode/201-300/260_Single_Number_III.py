__author__ = 'Yann.Xia'


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None:
            return []

        result = 0
        for n in nums:
            result ^= n

        last_1_bit = result - (result & (result - 1))
        sing_a = 0
        sing_b = 0

        for n in nums:
            if last_1_bit & n == 0:
                sing_a ^= n
            else:
                sing_b ^= n

        return [sing_a, sing_b]


s = Solution()

#print(s.singleNumber([1, 2, 1, 3, 2, 5]))
#print(s.singleNumber([-1, 0]))
print(s.singleNumber([-1139700704, -1653765433]))
print(s.singleNumber([0, 0, 1, 2]))
print(s.singleNumber([-1139700704, -1653765433]))
