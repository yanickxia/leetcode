import unittest


class Solution:
    def totalMoney(self, n: int) -> int:
        start = 1
        n_round = 0
        total = 0
        for i in range(0, n):
            if i % 7 == 0:
                n_round += 1
                start = n_round
            else:
                start += 1
            total += start
        return total


class TestSolution(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.totalMoney(4), 10)
        self.assertEqual(s.totalMoney(10), 37)
        self.assertEqual(s.totalMoney(20), 96)


if __name__ == '__main__':
    unittest.main()
