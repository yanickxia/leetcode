from typing import List


# 和一个无穷大的点对比

class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        stack = []
        res = 0
        for i, a in enumerate(A):
            if not stack or stack[-1][1] > a:
                stack.append((i, a))
            else:
                x = len(stack) - 1
                while x >= 0 and stack[x][1] <= a:
                    res = max(res, i - stack[x][0])
                    x -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.maxWidthRamp([0, 1]) == 1)
    # print(s.maxWidthRamp([4, 3, 2, 1, 0]) == 0)
    # print(s.maxWidthRamp([6, 0, 8, 2, 1, 5]) == 4)
    print(s.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7)
