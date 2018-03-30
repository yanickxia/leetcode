# -*- coding:utf-8 -*-

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        result = []
        for i, c in enumerate(input):
            if c in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        result.append(eval(str(l) + c + str(r)))
        return result


s = Solution()
print(s.diffWaysToCompute("2-1-1"))
print(s.diffWaysToCompute("2*3-4*5"))
