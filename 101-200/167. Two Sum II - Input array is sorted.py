from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i != j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            else:
                i += 1


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([1, 2, 3, 4, 5], 4))
