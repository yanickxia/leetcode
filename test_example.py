import unittest


class Solution:
    def fail(self) -> bool:
        return False


class TestSolution(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertFalse(s.fail())


if __name__ == '__main__':
    unittest.main()
