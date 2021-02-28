from typing import List


###
#
# i,j -> Max Satisfaction At Rang(i,j)
# F(i,j) -> Max( Max(F(i,j-1), F(i,j-1)+ S[j-1]*j), Max(F(i+1,j), F(i+1,j) + S[i] ))
#        -> Max(0,S[i-1]*i) IF i == j
###

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        i, j, n = 1, 1, len(satisfaction) + 1
        max_satisfaction = [[0 for j in range(n)] for i in range(n)]
        for i in range(1, n):
            for j in range(1, n):
                if i == j:
                    max_satisfaction[i][i] = max(0, satisfaction[i - 1])

        for k in range(1, n):
            for i in range(1, n - k):
                for j in range(i + k, n):
                    max_satisfaction[i][j] = max(
                        max(max_satisfaction[i][j - 1], max_satisfaction[i][j - 1] + ((j - i) * satisfaction[j - 1])),
                        max(max_satisfaction[i + 1][j], max_satisfaction[i + 1][j] + satisfaction[i])
                    )

        print(max_satisfaction)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSatisfaction([-1, -8, 0, 5, -9]))
