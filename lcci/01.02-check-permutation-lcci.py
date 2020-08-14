class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        chars = {}
        for i in range(len(s1)):
            c = s1[i]
            if c not in chars:
                chars[c] = 0
            chars[c] += 1

        for i in range(len(s2)):
            c = s2[i]
            if c not in chars:
                return False
            chars[c] -= 1
            if chars[c] == 0:
                del chars[c]

        return len(chars) == 0


