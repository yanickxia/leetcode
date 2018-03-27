# -*- coding:utf-8 -*-

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        is_negative_dividend = False
        if dividend < 0:
            is_negative_dividend = True
        is_negative_divisor = False
        if divisor < 0:
            is_negative_divisor = True

        dividend = abs(dividend)
        divisor = abs(divisor)

        str_dividend, str_divisor = str(dividend), str(divisor)
        # if str_dividend bigger than str_divisor
        if len(str_divisor) > len(str_dividend):
            return 0

        len_divisor = len(str_divisor)
        rs_array = []

        head_str_dividend = str_dividend[:len_divisor]
        remainder_str_dividend = str_dividend[len_divisor:]
        head_int_divisor = int(head_str_dividend)
        rs, remainder = self.same_len_number_divide(head_int_divisor, divisor)
        rs_array.append(rs)

        while len(remainder_str_dividend) > 0:
            str_dividend = str(remainder) + remainder_str_dividend[0]
            remainder_str_dividend = remainder_str_dividend[1:]
            rs, remainder = self.same_len_number_divide(int(str_dividend), divisor)
            rs_array.append(rs)

        x = int(''.join(str(e) for e in rs_array))

        if is_negative_dividend and is_negative_divisor:
            if x > 2147483647:
                x = 2147483647
            return x
        elif is_negative_dividend or is_negative_divisor:
            if x > 2147483648:
                x = 2147483648
            return -x
        else:
            if x > 2147483647:
                x = 2147483647
            return x

    def same_len_number_divide(self, x, y):
        c = 0
        while x >= y:
            x -= y
            c += 1
        return c, x


s = Solution()
print(s.divide(-2147483648,
      1))
