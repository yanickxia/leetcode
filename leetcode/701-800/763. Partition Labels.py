from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterIndex = {}
        for i in range(0, len(s)):
            letter = s[i]
            if letter not in letterIndex:
                letterIndex[letter] = []
            letterIndex[letter].append(i)
        ret = []
        start = 0
        while start < len(s):
            end = self.findlast(letterIndex, s, start)
            ret.append(end - start + 1)
            start = end + 1
        return ret

    def findlast(self, index, s, i):
        start = index[s[i]][0]
        end = index[s[i]][-1]
        atLast = end
        while True:
            for i in range(start + 1, end):
                if index[s[i]][-1] > atLast:
                    atLast = index[s[i]][-1]
            if atLast == end:
                return end
            end = atLast


if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels("qiejxqfnqceocmy"))
    print(s.partitionLabels("ababcbacadefegdehijhklij"))
    print(s.partitionLabels("eccbbbbdec"))
