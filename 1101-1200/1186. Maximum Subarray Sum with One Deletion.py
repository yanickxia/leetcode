from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        narr = []
        flag = False
        right_index = []
        atLeast = -float('inf')
        for i in range(0, len(arr)):
            if arr[i] > atLeast:
                atLeast = arr[i]
            if arr[i] >= 0:
                if flag:
                    narr[-1] += arr[i]
                else:
                    narr.append(arr[i])
                    right_index.append(len(narr) - 1)
                flag = True
            else:
                narr.append(arr[i])
                flag = False
        if len(right_index) == 0:
            return atLeast

        ans = -float('inf')
        for i in right_index:
            if i + 2 < len(narr):
                ans = max(narr[i], narr[i] + narr[i + 2], ans)
            else:
                ans = max(narr[i], ans)

        print(ans)
        return ans


if __name__ == '__main__':
    s = Solution()

    s.maximumSum([8, -1, 6, -7, -4, 5, -4, 7, -6])
    s.maximumSum([1, -2, 0, 3])
    s.maximumSum([1, -2, -2, 3])
    s.maximumSum([1, -1, -1, -1])
    s.maximumSum([0, -5, -6, 5, 0, -5])
    s.maximumSum([2, 1, -2, -5, -2])
