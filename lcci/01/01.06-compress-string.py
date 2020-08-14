class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S

        compressed = ""

        cur = S[0]
        i = 0
        while i < len(S):
            count = 0
            while count+i < len(S) and  S[count+i] == cur:
                count+=1
            compressed += cur + str(count)
            i += count
            if i >= len(S):
                break
            cur = S[i]
        return compressed if len(compressed) < len(S) else S
if __name__ == '__main__':
    s = Solution()
    print(s.compressString("aabcccccaaa") == "a2b1c5a3")
    print(s.compressString("abbccd") == "abbccd")
