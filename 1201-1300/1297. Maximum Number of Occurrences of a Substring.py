class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        max_count = 0
        for curSize in range(minSize, maxSize + 1):
            sub_dict = {}
            for i in range(0, len(s) - minSize + 1):
                subs = s[i:i + curSize]
                if subs in sub_dict:
                    sub_dict[subs] += 1
                else:
                    sub_dict[subs] = 1

            for (k, v) in sub_dict.items():
                if v > max_count and len(set([x for x in k])) <= maxLetters:
                    max_count = v
        return max_count


if __name__ == '__main__':
    s = Solution()
    print(s.maxFreq("aababcaab", 2, 3, 4))
    print(s.maxFreq("aaaa", 1, 3, 3))
    print(s.maxFreq("aabcabcab", 2, 2, 3))
    print(s.maxFreq("abcde", 2, 3, 3))
