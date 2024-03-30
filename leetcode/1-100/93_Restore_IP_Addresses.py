# -*- coding:utf-8 -*-
import unittest


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(1, 4):
            section = s[0:i]
            if Solution.is_vaild_address(section):
                result.extend(Solution.parseIpAddress(s[i:], 3, [section]))
        return result

    @staticmethod
    def parseIpAddress(s, r_count, rs):
        if r_count == 1:
            if Solution.is_vaild_address(s):
                return Solution.append_one(rs, s)
            else:
                return []

        this_rs = []
        for i in range(1, 4):
            ip_range = s[0:i]
            if Solution.is_vaild_address(ip_range):
                t_rs = Solution.append_one(rs, ip_range)

                s_rs = Solution.parseIpAddress(s[i:], r_count - 1, t_rs)
                this_rs.extend(s_rs)
        return this_rs

    @staticmethod
    def is_vaild_address(x):
        if x is "": return False
        if len(x) > 1 and x[0] == '0': return False
        return 0 <= int(x) < 256

    @staticmethod
    def append_one(rs, x):
        nrs = []
        for item in rs:
            item += "." + x
            nrs.append(item)
        return nrs


class TestStringMethods(unittest.TestCase):

    def test_restoreIpAddresses(self):
        s = Solution()
        self.assertEqual(s.restoreIpAddresses("25525511135"), ["255.255.11.135", "255.255.111.35"])
        self.assertEqual(s.restoreIpAddresses("1111"), ["1.1.1.1"])
        self.assertEqual(s.restoreIpAddresses("010010"), ["0.10.0.10", "0.100.1.0"])


if __name__ == '__main__':
    unittest.main()
