class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ns = sorted([1000, 500, 100, 50, 10, 5, 4, 1, 9, 49, 99, 499, 999, 40, 90, 490, 990, 400, 900], reverse=True)
        rs = ''
        while num != 0:
            for n in ns:
                while num % n == 0 and num != 0:
                    num -= n
                    rs += Solution.getStrFromInt(n)
                while num > n:
                    num -= n
                    rs += Solution.getStrFromInt(n)
        return rs

    @staticmethod
    def getStrFromInt(i):
        if i == 1:
            return 'I'
        elif i == 5:
            return 'V'
        elif i == 10:
            return 'X'
        elif i == 50:
            return 'L'
        elif i == 100:
            return 'C'
        elif i == 500:
            return 'D'
        elif i == 1000:
            return 'M'
        elif i == 4:
            return 'IV'
        elif i == 9:
            return 'IX'
        elif i == 49:
            return 'IL'
        elif i == 99:
            return 'IC'
        elif i == 499:
            return 'ID'
        elif i == 999:
            return 'IM'
        elif i == 40:
            return 'XL'
        elif i == 90:
            return 'XC'
        elif i == 490:
            return 'XD'
        elif i == 990:
            return 'XM'
        elif i == 400:
            return 'CD'
        elif i == 900:
            return 'CM'


s = Solution()
assert s.intToRoman(1980) == 'MCMLXXX'
assert s.intToRoman(3) == 'III'
assert s.intToRoman(4) == 'IV'
assert s.intToRoman(6) == 'VI'
assert s.intToRoman(19) == 'XIX'
assert s.intToRoman(19) == 'XIX'
assert s.intToRoman(20) == 'XX'
assert s.intToRoman(45) == 'XLV'
