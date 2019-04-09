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

        all_res = {}

        for i in range(len(s)):
            c = s[i]
            numbers = self.numbers_char_map.get(c)

            for ns in numbers:
                all_item = all_res.get(ns)
                if all_item is None:
                    all_res[ns] = [0] * len(ns)

                index_i_list = self.index_c_in_string(c, ns)
                if len(index_i_list) == 1:
                    all_res[ns][index_i_list[0]] += 1
                else:
                    is_set = False
                    for i in range(len(index_i_list) - 1):
                        if all_res[ns][index_i_list[i]] <= all_res[ns][index_i_list[i + 1]]:
                            all_res[ns][index_i_list[i]] += 1
                            is_set = True
                    if not is_set:
                        all_res[ns][index_i_list[len(index_i_list) - 1]] += 1

        rs = []
        for k, v in all_res.items():
            mv = min(v)
            while mv > 0:
                rs.append(k)

                #remove
                for c in k:


                mv -= 1
        x_n = [self.numbers_number.get(x) for x in rs]

        return "".join([str(e) for e in sorted(x_n)])

    def index_c_in_string(self, c, s):
        k = str(c + "_" + s)
        if self.index_cache.get(k) is None:
            rs = []
            for i in range(len(s)):
                if s[i] == c:
                    rs.append(i)
            self.index_cache[k] = rs

        return self.index_cache.get(k)


if __name__ == '__main__':
    s = Solution()
    print s.originalDigits("zeroonetwothreefourfivesixseveneightnine")
    print s.originalDigits("owoztneoer")
    print s.originalDigits("fviefuro")
    print s.originalDigits("ereht")
    print s.originalDigits("egith")
