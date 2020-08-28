from typing import List


# 5Min
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        status = "UP"
        if not A or len(A) < 3:
            return False

        i, j = 0, 1
        while j < len(A) and A[j] > A[i]:
            j += 1
            i += 1

        if j >= len(A) or i == 0:
            return False
        # DOWN
        while j < len(A) and A[j] < A[i]:
            j += 1
            i += 1

        if j != len(A):
            return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.validMountainArray([3, 5, 5]))
    print(s.validMountainArray([0, 3, 2, 1]))
    print(s.validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
