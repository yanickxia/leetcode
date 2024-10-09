# Given two non-negative integers low and high. Return the count of odd numbers 
# between low and high (inclusive). 
# 
#  
#  Example 1: 
# 
#  
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7]. 
# 
#  Example 2: 
# 
#  
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9]. 
# 
#  
#  Constraints: 
# 
#  
#  0 <= low <= high <= 10^9 
#  
# 
#  Related Topics Math 👍 2755 👎 158


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        begin_is_odd = low % 2 == 1
        end_is_odd = high % 2 == 1
        total = 0
        if begin_is_odd:
            total = 1

        total_num = high - low
        if total_num % 2 == 0:
            return total_num // 2 + total
        else:
            if end_is_odd:
                return total_num // 2 + total + 1
            else:
                return total_num // 2 + total


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.countOdds(14, 17))
