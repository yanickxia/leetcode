class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        S = S[:length]
        return ''.join(['%20' if x == " " else x  for x in list(S)])


if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpaces("Mr John Smith    ",13))