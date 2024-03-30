# -*- coding:utf-8 -*-


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        an = list(a)[::-1]
        bn = list(b)[::-1]
        cn = []
        for i in range(0, max(len(an), len(bn))):
            if i < len(an) and i < len(bn):
                c = int(an[i]) + int(bn[i])
                cn.append(c)
            elif i < len(an):
                cn.append(int(an[i]))
            elif i < len(bn):
                cn.append(int(bn[i]))

        carry = 0
        for i in range(0, len(cn)):
            c = cn[i] + carry
            if c >= 2:
                c = c % 2
                carry = 1
                cn[i] = c
            else:
                cn[i] = c
                carry = 0
        if carry == 1:
            cn.append(1)

        return ''.join(map(str, cn[::-1]))


s = Solution()
# print s.addBinary("11", "1")
# print s.addBinary("111", "1")
# print s.addBinary("0", "0")
# print s.addBinary("1111", "1111")
print s.addBinary("1010", "1011")
