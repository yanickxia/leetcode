from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0



        max_height = max(height)
        all = 0
        for h in range(1, max_height + 1):
            i, j = 0, len(height) - 1
            while height[i] < h:
                i += 1
            while height[j] < h:
                j -= 1

            all = sum(1 for x in height[i:j + 1] if x < h)
        return all


if __name__ == '__main__':
    s = Solution()
    print(s.trap([4,2,3]))
    print(s.trap([]))
    print(s.trap([2]))
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
