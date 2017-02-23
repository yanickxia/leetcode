# -*- coding:utf-8 -*-


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []


        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        rs = [""]
        for digit in digits:
            letter_array = letters.get(digit)
            new_rs = []
            for letter in letter_array:
                for r in rs:
                    new_rs.append(r + letter)
            rs = new_rs
        return rs

s = Solution()
print s.letterCombinations("23")
