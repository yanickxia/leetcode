import unittest


# 1 ->   1
# 2 ->  10
# 3 ->  11
# 4 -> 100
# 5 -> 101
# 6 -> 110
# 7 -> 111

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left

        b_left, b_right = bin(left)[2:], bin(right)[2:]
        if len(b_left) != len(b_right):
            return 0
        diff_index = -1
        for i in range(0, len(b_left)):
            if b_left[i] != b_right[i]:
                diff_index = i
                break

        b_right = b_right[0:diff_index] + ('0' * (len(b_right) - diff_index))
        b_right = b_right

        # print(int(b_right, 2))
        return int(b_right, 2)


class TestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual(s.rangeBitwiseAnd(4, 7), 4)
        self.assertEqual(s.rangeBitwiseAnd(1, 1), 1)
        self.assertEqual(s.rangeBitwiseAnd(5, 7), 4)
        self.assertEqual(s.rangeBitwiseAnd(0, 0), 0)
        self.assertEqual(s.rangeBitwiseAnd(1, 2147483647), 0)


if __name__ == '__main__':
    unittest.main()
