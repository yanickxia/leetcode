from typing import List


class Solution:

    def __init__(self):
        self.rs = 0

    def numTilePossibilities(self, tiles: str) -> int:
        chars = [0] * 26
        for i in range(len(tiles)):
            chars[ord(tiles[i]) - ord('A')] += 1

        def backtrack(cs: List[int]):
            for i in range(26):
                if cs[i] == 0:
                    continue
                self.rs += 1
                cs[i] -= 1
                backtrack(cs)
                cs[i] += 1

        backtrack(chars)
        return self.rs


if __name__ == '__main__':
    s = Solution()
    print(s.numTilePossibilities('AAB'))
