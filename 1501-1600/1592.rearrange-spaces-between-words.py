#
# @lc app=leetcode id=1592 lang=python3
#
# [1592] Rearrange Spaces Between Words
#

# @lc code=start


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()

        spaces = len([x for x in text if x == " "])
        if len(words) == 1:
            return words[0] + " " * spaces
        should = int(spaces / (len(words) - 1))
        insert = " " * should

        remain = spaces % (len(words) - 1)
        return insert.join(words) + " " * remain


# @lc code=end

s = Solution()
print(s.reorderSpaces("a"))
print(s.reorderSpaces("  this   is  a sentence "))
