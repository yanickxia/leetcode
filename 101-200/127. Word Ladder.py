class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList:
            return 0
        rs = []
        for i in range(len(beginWord)):
            may_next = list(beginWord)
            may_next[i] = endWord[i]
            may_next = ''.join(may_next)

            if may_next in wordList:
                v = self.ladderLength(may_next, endWord, wordList) + 1
                rs.append(v)
        return min(rs)


if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
