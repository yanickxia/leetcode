class Solution:
    def convertToTitle(self, n: int) -> str:
        chars = ['']
        for i in range(ord('A'), ord('Z') + 1):
            chars.append(chr(i))
        rs = ''
        while n > 26:
            k = n
            tmp = 1
            while k > 26:
                k = int(k/26)
                tmp *= 26
            rs += chars[k]
            n = n - tmp
        rs += chars[n]
        return rs
if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(701))
    print(s.convertToTitle(28))
