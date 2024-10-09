# You are given two 0-indexed strings word1 and word2. 
# 
#  A move consists of choosing two indices i and j such that 0 <= i < word1.
# length and 0 <= j < word2.length and swapping word1[i] with word2[j]. 
# 
#  Return true if it is possible to get the number of distinct characters in 
# word1 and word2 to be equal with exactly one move. Return false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: word1 = "ac", word2 = "b"
# Output: false
# Explanation: Any pair of swaps would yield two distinct characters in the 
# first string, and one in the second string.
#  
# 
#  Example 2: 
# 
#  
# Input: word1 = "abcc", word2 = "aab"
# Output: true
# Explanation: We swap index 2 of the first string with index 0 of the second 
# string. The resulting strings are word1 = "abac" and word2 = "cab", which both 
# have 3 distinct characters.
#  
# 
#  Example 3: 
# 
#  
# Input: word1 = "abcde", word2 = "fghij"
# Output: true
# Explanation: Both resulting strings will have 5 distinct characters, 
# regardless of which indices we swap.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= word1.length, word2.length <= 10⁵ 
#  word1 and word2 consist of only lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Counting 👍 570 👎 147

# 因为只能置换一次，尝试从 word1 中置换 a..z 和 word2 中置换 a ..z ,如果一样多就可以

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        w1_chars, w2_chars = {}, {}
        for c in word1:
            w1_chars[c] = w1_chars.get(c, 0) + 1
        for c in word2:
            w2_chars[c] = w2_chars.get(c, 0) + 1

        for i in range(ord('a'), ord('z') + 1):
            w1_replace = chr(i)
            for j in range(ord('a'), ord('z') + 1):
                w2_replace = chr(j)

                # 都存在，进行交换
                if w1_replace in w1_chars and w1_chars[w1_replace] > 0 and w2_replace in w2_chars and w2_chars[w2_replace] > 0:
                    w1_chars[w1_replace] -= 1
                    w1_chars[w2_replace] = w1_chars.get(w2_replace, 0) + 1
                    w1_different_chars = len({k: v for k, v in w1_chars.items() if v > 0})

                    w2_chars[w2_replace] -= 1
                    w2_chars[w1_replace] = w2_chars.get(w1_replace, 0) + 1
                    w2_different_chars = len({k: v for k, v in w2_chars.items() if v > 0})

                    if w1_different_chars == w2_different_chars:
                        return True

                    # rollback
                    w1_chars[w1_replace] += 1
                    w1_chars[w2_replace] -= 1

                    w2_chars[w2_replace] += 1
                    w2_chars[w1_replace] -= 1
        return False


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.isItPossible("", ""))
