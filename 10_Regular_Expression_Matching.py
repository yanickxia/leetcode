# -*- coding:utf-8 -*-
from unittest import TestCase

class Solution(object):
    def __init__(self):
        self.root = None

    def isMatch(self, text, reg):
        """
        :type text: str
        :type reg: str
        :rtype: bool
        """


class DFA(object):
    def compile(self, pattern):
        




class SolutionTest(TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.isMatch("aa", "a*"))
        self.assertFalse(s.isMatch("ab", ".*c"))
        self.assertFalse(s.isMatch("aa", "a"))
        self.assertTrue(s.isMatch("", ".*"))

        self.assertFalse(s.isMatch("aaa", "aa"))
        self.assertTrue(s.isMatch("aa", "aa"))
        self.assertTrue(s.isMatch("aa", ".*"))
        self.assertTrue(s.isMatch("aa", ".*"))
        self.assertTrue(s.isMatch("aa", "c*a*b"))


        # a(bb)+a -> abb.+.a.
        # a?a?aa -> a?a?.a.a.
