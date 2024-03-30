class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        while k > 0:
            num = self.removeDigit(num)
            k -= 1
        return num

    def removeDigit(self, num: str) -> str:
        if len(num) == 1:
            return "0"

        removed = -1
        for i in range(0, len(num) - 1):
            if int(num[i]) > int(num[i + 1]):
                removed = i
                break

        if removed == -1:
            if num[-1] > num[0]:
                removed = len(num) - 1
            else:
                removed = 0

        return str(int(num[0:removed] + num[removed + 1:]))


if __name__ == '__main__':
    s = Solution()
    print(s.removeKdigits("112", 1))
    print(s.removeKdigits("1432219", 3))
    print(s.removeKdigits("10200", 1))
    print(s.removeKdigits("10", 2))
