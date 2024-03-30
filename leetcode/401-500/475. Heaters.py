# -*- coding:utf-8 -*-


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        ans = 0
        pos = 0
        heaters = [float('-inf')] + heaters + [float('inf')]
        for house in houses:
            while house >= heaters[pos]:
                pos += 1
            r = min(house - heaters[pos - 1], heaters[pos] - house)
            ans = max(ans, r)
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.findRadius([1, 2, 3], [2])
    print s.findRadius([1, 2, 3, 4], [1, 4])
