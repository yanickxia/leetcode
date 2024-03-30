from typing import List


# 18Min
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        if not A:
            return 0


        # F(N) = F(N-1) - SUM(A) + N * A[N-1]

        f0, sumA = 0, sum(A)
        for i in range(len(A)):
            f0 += i * A[i]

        maxium = f0
        fi = f0
        for i in range(1, len(A)):
            fi = fi - sumA + len(A) * A[i-1]
            maxium = max(fi, maxium)

        return maxium

if __name__ == '__main__':
    s = Solution()
    print(s.maxRotateFunction([4,3,2,6]))