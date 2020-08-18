class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        tem = "1" * (32 - j - 1) + "0" * (j - i + 1) + "1" * i
        # 将N的i-j为置0
        # 将M左移i位
        # 两者相或即可
        return (int(tem, base=2) & N) | (M << i)

if __name__ == '__main__':
    s = Solution()
    print(s.insertBits(1024, 19, 2, 6) == 1100)
    print(s.insertBits(0, 31, 0, 4) == 31)
    print(s.insertBits(2032243561, 10, 24, 29) == 1243714409)
    print(s.insertBits(1143207437, 1017033, 11, 31))
