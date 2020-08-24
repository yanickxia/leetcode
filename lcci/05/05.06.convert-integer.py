
# 15 min
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        res = 0
        c = A ^ B
        for i in range(32):
            res += c >> i & 1
        return res




if __name__ == '__main__':
    s = Solution()
    print(s.convertInteger(826966453, -729934991))
    print(s.convertInteger(1, 2))
    print(s.convertInteger(29, 15))
