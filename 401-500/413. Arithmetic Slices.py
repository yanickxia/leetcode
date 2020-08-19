from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        l, n = 2, len(A)
        rs = 0
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                l += 1
            else:
                rs += (l-1)*(l-2) * 0.5 if l > 2 else 0
                l = 2

        rs += (l - 1) * (l - 2) * 0.5 if l > 2 else 0
        return int(rs)
