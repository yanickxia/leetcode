class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0;


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(9))
    print(s.isPowerOfThree(27))
    print(s.isPowerOfThree(0))
    print(s.isPowerOfThree(45))
