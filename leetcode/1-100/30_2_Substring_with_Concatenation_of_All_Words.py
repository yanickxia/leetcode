import copy


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        word_len = len(words[0])
        words_count = len(words)
        words_sum = Solution.sum_of_words(words)
        unique_map = Solution.words_to_unique_map(words)
        split_by_word_length_s = Solution.split_by_length(s, word_len)
        mathc_arrays_v = []
        for split_s in split_by_word_length_s:
            if split_s in unique_map:
                mathc_arrays_v.append(unique_map.get(split_s))
            else:
                mathc_arrays_v.append(0)

        rs = []
        for i in range(0, len(mathc_arrays_v)):
            if sum(mathc_arrays_v[i:i + words_count]) == words_sum:
                rs.append(i * word_len)

        return rs

    @staticmethod
    def sum_of_words(words):
        s = 0
        for word in words:
            s += sum([ord(c) for c in word])
        return s

    @staticmethod
    def find_from_index(s, i, word_len, unique_map):
        next_word = s[i:i + word_len]
        while next_word in unique_map and unique_map[next_word] > 0:
            unique_map[next_word] = unique_map[next_word] - 1
            i += word_len
            next_word = s[i:i + word_len]

        return Solution.check_unique_map(unique_map)

    @staticmethod
    def check_unique_map(unique_map):
        for n in unique_map.keys():
            if unique_map[n] != 0:
                return False
        return True

    @staticmethod
    def words_to_unique_map(words):
        unique_map = {}
        for word in words:
            x = sum([ord(c) for c in word])
            unique_map[word] = x
        return unique_map

    @staticmethod
    def split_by_length(s, block_size):
        w = []
        n = len(s)
        for i in range(0, n, block_size):
            w.append(s[i:i + block_size])
        return w


print(Solution.words_to_unique_map(["foo", "bar", "the"]))

s = Solution()
print(s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"]))
print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(s.findSubstring("barfoofoobarthefoobarman", ["foo", "bar", "the"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
