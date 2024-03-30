from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        rs = {}
        for i in range(len(s) - 9):
            sub = s[i:i + 10]
            if sub in rs:
                rs[sub] += 1
            else:
                rs[sub] = 1

        rs = [x for x in rs if rs[x] > 1]

        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))
    print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

