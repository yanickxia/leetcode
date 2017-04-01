# -*- coding:utf-8 -*-





class Solution(object):
    def __init__(self):
        self.gen_rs = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        start = ["("]
        self.appendParenthesis(start, n)
        return self.gen_rs

    def appendParenthesis(self, rs, n):

        if len(rs[0]) == 2 * n:
            self.gen_rs = rs
        else:
            inner_rs = []
            for item in rs:
                count_left = len([x for x in item if x == "("])
                count_right = len([x for x in item if x == ")"])
                if count_left == n:
                    inner_rs.append(item + ")")
                else:
                    if item[-1] == '(':
                        inner_rs.append(item + ")")
                        inner_rs.append(item + "(")
                    else:
                        if count_left == count_right:
                            inner_rs.append(item + "(")
                        else:
                            inner_rs.append(item + ")")
                            inner_rs.append(item + "(")

            rs = inner_rs
            self.appendParenthesis(rs, n)


s = Solution()
print s.generateParenthesis(3)

print sorted(["(())()", ])

print sorted([])
