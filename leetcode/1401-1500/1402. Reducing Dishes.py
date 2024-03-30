from typing import List

"""
最终上菜的顺序肯定是从小到大

逆序累加，第二轮要因为时间价值 +1，因此要把之前加过的值都再加一遍，当某一次我们加上 负值菜 没有收益的时候，就可以提前终结了

"""


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        i, j, n = 1, 1, len(satisfaction)
        satisfaction.sort()

        ans, append = 0, 0
        for n in range(n, 0, -1):
            this = ans + append + satisfaction[n - 1]
            if this < ans:
                return ans
            ans = this
            append += satisfaction[n - 1]

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxSatisfaction([-1, -8, 0, 5, -9]))
