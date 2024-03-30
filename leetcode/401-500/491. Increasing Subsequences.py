from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(0, len(nums) - 1):
            fst = nums[i]
            for j in range(i+1, len(nums)):
                sec = nums[j]
                if sec >= fst:
                    result = self.findSeq(nums, j+1, [fst, sec])
                    result.append([fst, sec])
                    ans.extend(result)

        return self._removeDump(ans)

    def _removeDump(self, nums: List[List[int]]) -> List[List[int]]:
        cache = {}
        ans = []
        for num in nums:
            numTmp = str(num)
            if numTmp not in cache:
                cache[numTmp] = True
                ans.append(num)
        return ans

    def findSeq(self, nums: List[int], startAt: int, before: List[int]) -> List[List[int]]:
        ans = [before]

        if startAt == len(nums):
            return ans
        
        for i in range(startAt, len(nums)):
            c = nums[i]
            if c >= before[-1]:
                tmp = list(before)
                tmp.append(c)
                result = self.findSeq(nums, i+1, tmp)
                ans.extend(result)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findSubsequences([4, 6, 7, 7]))
    print(s.findSubsequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]))
