# -*- coding:utf-8 -*-
from unittest import TestCase


class Solution:
    def longestPalindrome(self, s: str) -> str:

        i, j, longest = 0, 0, -1
        result = ()
        # find first longest
        while i < len(s) and j <= len(s):
            if Solution.isPalindrome(s[i:j]):
                if (j - i) > longest:
                    longest = (j - i)
                    result = (i, j)
            j += 1

        while i < len(s):
            i += 1
            j = i + longest
            while i < len(s) and j <= len(s):
                if Solution.isPalindrome(s[i:j]):
                    if (j - i) > longest:
                        longest = (j - i)
                        result = (i, j)
                j += 1

        return s[result[0]: result[1]]

    @staticmethod
    def isPalindrome(s: str):
        return s[::-1] == s


class SolutionTest(TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.longestPalindrome('a'), 'a')
        self.assertEqual(s.longestPalindrome('aa'), 'aa')

        # self.assertEqual(s.longestPalindrome('aba'), 'aba')
        # self.assertEqual(s.longestPalindrome('abc'), 'a')
        # self.assertEqual(s.longestPalindrome('abbac'), 'abba')
        # self.assertEqual('sknks', s.longestPalindrome('sknks'))
        # self.assertEqual(s.longestPalindrome(
        #     "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"),
        #     "sknks")

        self.assertEqual("ykdky",
                         s.longestPalindrome(
                             "iopsajhffgvrnyitusobwcxgwlwniqchfnssqttdrnqqcsrigjsxkzcmuoiyxzerakhmexuyeuhjfobrmkoqdljrlojjjysfdslyvckxhuleagmxnzvikfitmkfhevfesnwltekstsueefbrddxrmxokpaxsenwlgytdaexgfwtneurhxvjvpsliepgvspdchmhggybwupiqaqlhjjrildjuewkdxbcpsbjtsevkppvgilrlspejqvzpfeorjmrbdppovvpzxcytscycgwsbnmspihzldjdgilnrlmhaswqaqbecmaocesnpqaotamwofyyfsbmxidowusogmylhlhxftnrmhtnnljjhhcfvywsqimqxqobfsageysonuoagmmviozeouutsiecitrmkypwknorjjiaasxfhsftypspwhvqovmwkjuehujofiabznpipidhfxpoustquzyfurkcgmioxacleqdxgrxbldcuxzgbcazgfismcgmgtjuwchymkzoiqhzaqrtiykdkydgvuaqkllbsactntexcybbjaxlfhyvbxieelstduqzfkoceqzgncvexklahxjnvtyqcjtbfanzgpdmucjlqpiolklmjxnscjcyiybdkgitxnuvtmoypcdldrvalxcxalpwumfx"))
