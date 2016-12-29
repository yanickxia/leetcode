# -*- coding:utf-8 -*-
from unittest import TestCase

SPITE = "SPITE"
MATCH = "MATCH"
ANY = "ANY"


class State:
    def __init__(self):
        self.c = ''
        self.out = State


class Solution(object):
    def __init__(self):
        self.root = None

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

    def gen_state(self, p):
        i, p_size = 0, len(p)
        current_state = None
        while i < p_size:
            if str(p[i]).isalpha():
                if str(p[i + 1]).isalpha():
                    current_state = State
                    current_state.c = p[i]
                    i += 1
            if str(p[i + 1]) == '.':
                if str(p[i + 1]) == '*':
                    current_state.out =



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
