class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            if s[i] != ' ':
                j = 1
                while i + j < len(s) and s[i + j] != ' ':
                    j += 1

                result.append(s[i:i + j])
                i += j
            else:
                i += 1
        result.reverse()
        return ' '.join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("  hello world!  "))
    print(s.reverseWords("the sky is blue"))
