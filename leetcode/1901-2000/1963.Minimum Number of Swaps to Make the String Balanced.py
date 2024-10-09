# You are given a 0-indexed string s of even length n. The string consists of 
# exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'. 
# 
#  A string is called balanced if and only if: 
# 
#  
#  It is the empty string, or 
#  It can be written as AB, where both A and B are balanced strings, or 
#  It can be written as [C], where C is a balanced string. 
#  
# 
#  You may swap the brackets at any two indices any number of times. 
# 
#  Return the minimum number of swaps to make s balanced. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "][]["
# Output: 1
# Explanation: You can make the string balanced by swapping index 0 with index 3
# .
# The resulting string is "[[]]".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "]]][[["
# Output: 2
# Explanation: You can do the following to make the string balanced:
# - Swap index 0 with index 4. s = "[]][][".
# - Swap index 1 with index 5. s = "[[][]]".
# The resulting string is "[[][]]".
#  
# 
#  Example 3: 
# 
#  
# Input: s = "[]"
# Output: 0
# Explanation: The string is already balanced.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == s.length 
#  2 <= n <= 10⁶ 
#  n is even. 
#  s[i] is either '[' or ']'. 
#  The number of opening brackets '[' equals n / 2, and the number of closing 
# brackets ']' equals n / 2. 
#  
# 
#  Related Topics Two Pointers String Stack Greedy 👍 2061 👎 100


# leetcode submit region begin(Prohibit modification and deletion)

import math


class Solution:
    def minSwaps(self, s: str) -> int:
        # 想办法把下面这个操作加速
        # while '[]' in s:
        #     s = s.replace('[]', '')
        stack = [s[0]]
        i = 1
        while True:
            if i >= len(s):
                break
            current = s[i]
            if current == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                    i += 1
                    continue

            stack.append(current)
            i += 1
        s = ''.join(stack)
        if s == '':
            return 0
        return math.ceil(len(s) / 4)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(
        s.minSwaps("[[][[[[][][[[[]]][][]]]]][[][[][][]][[[[]]][[]][[]][[]]]]]]]][]][]]][[]][[[[[[][[]][[[][]][[]]]["))
