from typing import List

# 15Min
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_min(time: str):
            spited = time.split(":")
            return 60 * (int(spited[0])) + (int(spited[1]))

        full = 60 * 24
        times = [time_to_min(x) for x in timePoints]
        times = sorted(times)
        ans = float('inf')
        for i in range(len(times)):
            if i < len(times) - 1:
                d1 = abs(times[i + 1] - times[i])
                d2 = full - times[i + 1] + times[i]
                ans = min(ans, d1, d2)
            if i > 0:
                d1 = abs(times[i] - times[i - 1])
                d2 = full - times[i] + times[i - 1]
                ans = min(ans, d1, d2)

        ans = min(ans, full - times[-1] + times[0])

        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.findMinDifference(["05:31", "22:08", "00:35"]))
    print(s.findMinDifference(["23:59", "00:00"]) == 1)
