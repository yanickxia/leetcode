# -*- coding:utf-8 -*-
from unittest import TestCase


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        i, j, lenS = 0, 1, len(s)
        longest, longestLen = s[0], 1



        while i < lenS:

            if i == 529:
                print 111

            # if odd
            j = 1
            while i - j >= 0 and i + j < lenS:
                if s[i - j] == s[i + j]:
                    if 1 + 2 * j > longestLen:
                        longest = s[i - j:i + j + 1]
                        longestLen = len(longest)
                    j += 1
                else:
                    break

            j = 0
            # if Even
            if i + 1 < lenS and s[i] == s[i + 1]:
                while i - j >= 0 and i + j + 1 < lenS:
                    if s[i - j] == s[i + 1 + j]:
                        if 2 + 2 * j > longestLen:
                            longest = s[i - j:i + j + 2]
                            longestLen = len(longest)
                        j += 1
                    else:
                        break

            i += 1

        return longest


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
