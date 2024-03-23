class Solution:
    def cuttingRope(self, n: int) -> int:
        maximum = 0
        for x in range(2, n + 1):
            if n % x == 0:
                maximum = max(int(n / x) ** x, maximum)
            else:
                remain = n % x
                all = int(n / x)
                more = all - remain
                maximum = max((all ** (x - remain)) * ((all + 1) ** remain), maximum)
        return maximum


if __name__ == '__main__':
    s = Solution()
    print(s.cuttingRope(2))
    print(s.cuttingRope(10))
