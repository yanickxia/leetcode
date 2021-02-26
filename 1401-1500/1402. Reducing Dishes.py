from typing import List


###

# i,j -> Max Satisfaction At Rang(i,j)
# F(i,j) = Max(F(x-1), F(x-1) + (x * S[x-1]))
# F(1) = Max(0, 1*S[0])
# F(2) = Max(F(1), F(1) + 2 * S[1]), F()
###

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        max_satisfaction = [0] * (len(satisfaction) + 1)

