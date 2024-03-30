from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time_rem = [x % 60 for x in time]
        cache = {}
        for i in range(0, len(time_rem)):
            item = time_rem[i]
            if item not in cache:
                cache[item] = [i]
            else:
                cache[item].append(i)
        ans = 0
        for i in range(0, len(time_rem)):
            item = time_rem[i]
            rm = 60 - item
            if rm == 60:
                rm = 0

            if rm in cache:
                ans += len([x for x in cache[rm] if x > i])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numPairsDivisibleBy60([30, 20, 150, 100, 40]))
    print(s.numPairsDivisibleBy60([60, 60, 60]))
