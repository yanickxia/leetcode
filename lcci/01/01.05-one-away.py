class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if first == second:
            return True

        s1_len = len(first)
        s2_len = len(second)

        if abs(s1_len - s2_len) > 1:
            return False

        if len(first) == len(second):
            diff = 0
            for i in range(s1_len):
                if first[i] != second[i]:
                    diff += 1
                if diff > 1:
                    return False
            return True

        long = first if s1_len > s2_len else second
        short = first if s1_len < s2_len else second

        i, j = 0, 0
        while i < len(short) and j < len(long):
            if short[i] == long[j]:
                i += 1
                j += 1
            elif short[i] != long[j]:
                j+=1

            if j - i > 1:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.oneEditAway("intention", "execution") == False)
    print(s.oneEditAway("pale", "ple") == True)
    print(s.oneEditAway("ple", "pale") == True)
    print(s.oneEditAway("pales", "ple") == False)
    print(s.oneEditAway("a", "b") == True)
