class Solution:
    def reverseBits(self, n: int) -> int:
        rs = bin(n)[2:].rjust(32,'0')[::-1]
        return  (int(rs,2))


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(43261596))
    s.reverseBits(4294967293)