import unittest


class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ans = []
        while A > 0 and B > 0:
            ans.append('a')
            ans.append('b')
            A -= 1
            B -= 1

        if A + B == 0:
            return ''.join(ans)


        rs = []
        if A > 0:
            while ans:
                x = ans.pop()
                if x == 'a':
                    rs.append('aa')
                    A -= 1
                    if A == 0:
                        ans.reverse()
                        rs.extend(ans)
                        break
                else:
                    rs.append('b')
            if A == 2:
                rs = ['aa'] + rs
            if A == 1:
                rs = ['a'] + rs

        if B > 0:
            ans = ['b' if x == 'a' else 'a' for x in ans]
            while ans:
                x = ans.pop()
                if x == 'b':
                    rs.append('bb')
                    B -= 1
                    if B == 0:
                        ans.reverse()
                        rs.extend(ans)

                        break

                else:
                    rs.append('a')
            if B == 2:
                rs = ['bb'] + rs
            if B == 1:
                rs = ['b'] + rs

        return ''.join(rs)


class TestSolution(unittest.TestCase):
    def test(self):
        s = Solution()
        print(s.strWithout3a3b(2, 3))
        print(s.strWithout3a3b(1, 1))
        print(s.strWithout3a3b(1, 4))
        print(s.strWithout3a3b(4, 1))
        print(s.strWithout3a3b(0, 0))
        print(s.strWithout3a3b(1, 3))

        print(s.strWithout3a3b(1, 2))


if __name__ == '__main__':
    unittest.main()
