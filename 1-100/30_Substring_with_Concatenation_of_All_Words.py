import copy


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        word_len = len(words[0])
        unique_map = Solution.words_to_unique_map(words)

        index_array = []
        for i in range(0, len(s) - (word_len * len(words)) + 1):
            find_word = s[i:i + word_len]
            if find_word in unique_map:
                cp_of_unique_map = copy.deepcopy(unique_map)
                cp_of_unique_map[find_word] = cp_of_unique_map[find_word] - 1
                if Solution.find_from_index(s, i + word_len, word_len, cp_of_unique_map):
                    index_array.append(i)

        return index_array

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
            if word in unique_map:
                unique_map[word] = unique_map[word] + 1
            else:
                unique_map[word] = 1
        return unique_map


s = Solution()
# print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(s.findSubstring("barfoofoobarthefoobarman", ["foo", "bar", "the"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
