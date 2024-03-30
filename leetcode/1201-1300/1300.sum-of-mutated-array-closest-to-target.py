#
# @lc app=leetcode id=1300 lang=python3
#
# [1300] Sum of Mutated Array Closest to Target
#

# @lc code=start
from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        arr.sort()
        pre = 0
        for i in range(n):
            curr_sum = pre + (n - i) * arr[i]
            if curr_sum >= target:
                value = (target - pre) // (n - i)
                sum_low = pre + value * (n - i)
                sum_high = sum_low + n - i
                return value if (target - sum_low) <= (sum_high - target) else value + 1
            pre += arr[i]

        return arr[-1]
        # @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.findBestValue([2, 3, 5], 10) == 5)
    print(s.findBestValue([1547, 83230, 57084, 93444, 70879], 71237)) #17422
    print(s.findBestValue([60864, 25176, 27249, 21296, 20204], 56803) == 11361)
    print(s.findBestValue([4, 9, 3], 10) == 3)

        #arr.sort()
        # arr.reverse()
        #
        # # not in array
        # minium = int(target / len(arr))
        # mindiff = abs(minium * len(arr) - target)
        # maxdiff = abs((minium + 1) * len(arr) - target)
        # if mindiff < maxdiff:
        #     ans = minium
        #     diff = mindiff
        # else:
        #     ans = minium + 1
        #     diff = maxdiff
        #
        # oneway_sum = []
        # s = 0
        # for i in range(len(arr)-1,-1,-1):
        #     s += arr[i]
        #     oneway_sum.append(s)
        # oneway_sum.reverse()
        #
        # p = arr[0]
        # q = arr[0]
        # skipAt = 0
        # while p != arr[-1]:
        #     while p < arr[skipAt]:
        #         skipAt+=1
        #         if skipAt == len(arr):
        #             return ans
        #     x = skipAt * p + oneway_sum[skipAt]
        #     if abs(x - target) < diff:
        #         diff = abs(x-target)
        #         ans = p
        #     p -=1
