import unittest
from typing import List


# time cost
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1
        cp = [0] * len(A)
        for i in range(1, len(A)):
            cp[i] = 1 if A[i] > A[i - 1] else -1 if A[i] < A[i - 1] else 0
        i, j, ans = 0, 1, 0
        while j < len(A):
            if cp[j] == 0:
                ans = max(ans, 1)
                i = j
                j += 1
                continue
            if cp[j] == -cp[j - 1] or cp[j - 1] == 0:
                ans = max(ans, j - i + 1)
                # print(i, j)
                j += 1
            else:
                i = j - 1
                j = j + 1
        return ans


class TestSolution(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertIs(s.maxTurbulenceSize([0, 1, 1, 0, 1, 0, 1, 1, 0, 0]), 5)
        self.assertIs(s.maxTurbulenceSize([9, 9]), 1)
        self.assertIs(s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]), 5)
        self.assertIs(s.maxTurbulenceSize([4, 8, 12, 16]), 2)
        self.assertIs(s.maxTurbulenceSize([100]), 1)


if __name__ == '__main__':
    unittest.main()
