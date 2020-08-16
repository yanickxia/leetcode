from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        i = 0
        m = len(height)
        all = 0

        def calc(hs: List[int]) -> int:
            all = hs[0] * len(hs)
            for h in hs:
                all -= h
            return all if all > 0 else 0

        all_traps = []
        while i < m:
            j = 1

            trap = [height[i]]
            while i + j < m and height[j + i] <= height[i]:
                trap.append(height[i + j])
                j += 1

            all_traps.append(trap)

            i += j
        # last some different
        remind = 0
        if all_traps:
            trap = all_traps[-1]
            if trap[0] == trap[-1]:
                remind = calc(trap)
            else:
                trap.reverse()
                remind = self.trap(trap)


        for i in range(len(all_traps) - 1):
            all += calc(all_traps[i])

        return all + remind


if __name__ == '__main__':
    s = Solution()
    print(s.trap([4, 2, 3]))
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([2, 0, 2]))
    print(s.trap([]))
    print(s.trap([2]))
