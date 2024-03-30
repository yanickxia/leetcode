# -*- coding:utf-8 -*-

class Solution(object):

    def __init__(self):
        self.numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        self.numbers_number = {
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
        }
        self.numbers_char_map = {}
        for i in range(ord('a'), ord('z') + 1):
            c = chr(i)
            self.numbers_char_map[c] = [x for x in self.numbers if c in x]
        self.index_cache = {}

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = [0] * 10
        char_map = {}
        for i in range(ord('a'), ord('z') + 1):
            char_map[chr(i)] = 0
        for c in s:
            char_map[c] += 1

        rs[0] = char_map.get('z')
        rs[2] = char_map.get('w')
        rs[4] = char_map.get('u')
        rs[6] = char_map.get('x')
        rs[8] = char_map.get('g')
        rs[3] = char_map.get('h') - rs[8]
        rs[7] = char_map.get('s') - rs[6]
        rs[5] = char_map.get('v') - rs[7]
        rs[1] = char_map.get('o') - rs[0] - rs[2] - rs[4]
        rs[9] = (char_map.get('n') - rs[1] - rs[7]) / 2

        r_str = ""
        for i in range(10):
            r_str += str(i) * rs[i]

        return r_str


if __name__ == '__main__':
    s = Solution()
    print s.originalDigits("zeroonetwothreefourfivesixseveneightnine")
    print s.originalDigits("owoztneoer")
    print s.originalDigits("fviefuro")
    print s.originalDigits("ereht")
    print s.originalDigits("egith")
