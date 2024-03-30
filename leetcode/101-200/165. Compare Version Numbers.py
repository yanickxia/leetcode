class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        m = max(len(v1), len(v2))
        i = m - len(v1)
        while i > 0:
            v1.append('0')
            i -= 1
        i = m - len(v2)
        while i > 0:
            v2.append('0')
            i -= 1

        i = 0
        while i < m:
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1
            i += 1

        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion("1.0", "1"))
    print(s.compareVersion("1", "1.1"))
    print(s.compareVersion("7.5.2.4", "7.5.3"))
    print(s.compareVersion("1.1", "1.10"))
    print(s.compareVersion("01", "1"))
