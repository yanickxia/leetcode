# 5Min
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        else:
            ans = 1
            while ans % K != 0:
                ans = ans * 10 + 1
            return len(str(ans))
