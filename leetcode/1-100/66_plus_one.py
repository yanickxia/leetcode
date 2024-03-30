# -*- coding:utf-8 -*-

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] = digits[-1] + 1

        carry_flag = False
        for i in range(len(digits) - 1, -1, -1):
            n = 0

            if carry_flag:
                n = digits[i] + 1
                carry_flag = False
            else:
                n = digits[i]

            if n > 9:
                n = n % 10
                carry_flag = True

            digits[i] = n

        if carry_flag:
            digits = [1] + digits

        return digits


s = Solution()
print s.plusOne([1, 0])
print s.plusOne([8, 9, 9, 9])
