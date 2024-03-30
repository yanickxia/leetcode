from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        is_palindrome = lambda s: s == s[::-1]

        def dfs(currList, k):
            if k == len(s):
                ans.append(currList)
                return

            for i in range(k, len(s)):
                tmpStr = s[k:i + 1]
                if is_palindrome(tmpStr):
                    dfs(currList + [tmpStr], i + 1)

        dfs([], 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))