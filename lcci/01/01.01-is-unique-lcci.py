class Solution:
    def isUnique(self, astr: str) -> bool:
        for i in range(len(astr)):
            if astr[i] in astr[i+1:]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isUnique("abc"))