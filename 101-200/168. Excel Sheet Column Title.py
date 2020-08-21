class Solution:
    def convertToTitle(self, n: int) -> str:
        chars = ['']
        for i in range(ord('A'), ord('Z') + 1):
            chars.append(chr(i))
        rs = ''
        while n > 26:
            k = n
            c = 0
            while k > 26:
                k = int(k / 26)
                c += 1
            rs += chars[k]

            n = k - ((26 ** c) * 26)
        print(rs)
        return rs
if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(701))