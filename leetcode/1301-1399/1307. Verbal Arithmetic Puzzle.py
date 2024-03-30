from typing import List


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        result_len = len(result)
        words_adders = []
        chars_mapping = {}
        for i in range(0, result_len):
            words_adder = []
            for x in words:
                if len(x) > i:
                    words_adder.append(x[len(x) - i - 1])
                    chars_mapping[x[len(x) - i - 1]] = None

            if len(words_adder) > 0:
                words_adders.append(words_adder)

        result_words = list(result)
        result_words.reverse()
        ## Words Mapping

        return self.try_it(words_adders, chars_mapping, result_words, set(chars_mapping.keys()),
                           {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

    def try_it(self, words_adders, chars_mapping, result_words, leaves_chars, leaves_nums):
        if len(leaves_chars) == 0:
            # print(chars_mapping)
            return self.check_all(words_adders, chars_mapping, result_words, leaves_nums)

        for x in range(0, 10):
            if x not in leaves_nums:
                continue
            current_char = leaves_chars.pop()
            chars_mapping[current_char] = x
            leaves_nums.remove(x)

            result = self.try_it(words_adders, chars_mapping, result_words, leaves_chars, leaves_nums)
            if result:
                return result

            leaves_nums.add(x)
            leaves_chars.add(current_char)
        return False

    def array_to_sum(self, arr, chars_mapping):
        numbers = [chars_mapping[x] for x in arr]
        n = 0
        for i in range(0, len(numbers)):
            n = n + numbers[i]
        return n

    def check_all(self, words_adders, chars_mapping, result_words, leaves_nums):
        chars_mapping = chars_mapping.copy()
        leaves_nums = leaves_nums.copy()
        # if chars_mapping['D'] == 7 and chars_mapping['E'] == 5 and chars_mapping['N'] == 6 \
        #         and chars_mapping['R'] == 8 and chars_mapping['O'] == 0 and chars_mapping['S'] == 9 \
        #         and chars_mapping['M'] == 1:
        #     print("")

        carry = 0
        for i in range(0, len(words_adders)):
            n = self.array_to_sum(words_adders[i], chars_mapping)
            n += carry

            c = result_words[i]
            if c in chars_mapping:
                if n % 10 != chars_mapping[c]:
                    return False
            else:
                remind = n % 10
                if remind not in leaves_nums:
                    return False
                chars_mapping[c] = remind
                leaves_nums.remove(remind)

            carry = int(n / 10)

        if len(words_adders) != len(result_words):
            if result_words[-1] in chars_mapping:
                return carry == chars_mapping[result_words[-1]]
            else:
                return carry in leaves_nums

        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isSolvable(["SEND", "MORE"], "MONEY"))
    print(s.isSolvable(["SIX", "SEVEN", "SEVEN"], "TWENTY"))
    print(s.isSolvable(["THIS", "IS", "TOO"], "FUNNY"))
    print(s.isSolvable(["LEET", "CODE"], "POINT"))
    print(s.isSolvable(["TO", "CODE", "OR", "NOT", "TO"], "CODE"))
