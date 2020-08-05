from typing import List
from unittest import TestCase


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        i = 1

        words = sorted(words, key=len, reverse=True)

        writeds = [words[0]]
        while i != len(words):
            found = False
            word = words[i]
            for j in range(len(writeds)):
                if writeds[j].endswith(word):
                    # calc
                    found = True
                    break
            # calc
            if not found:
                writeds.append(word)
            i += 1
        return len('#'.join(writeds)) + 1


class TestSolution(TestCase):
    def test_minimum_length_encoding(self):
        s = Solution()
        self.assertEqual(s.minimumLengthEncoding(["time", "me", "bell"]), 10)
        self.assertEqual(s.minimumLengthEncoding(["me", "time"]), 5)


if __name__ == '__main__':
    t = TestSolution()
    t.test_minimum_length_encoding()
