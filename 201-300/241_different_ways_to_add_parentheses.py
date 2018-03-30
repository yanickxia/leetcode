# -*- coding:utf-8 -*-

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        x = self.to_array(input)

        return self.compute_reminder_array(x)

    def calc_str(self, a):
        rs, i = int(a[0]), 1
        while i < len(a):
            if a[i] == '+':
                rs += int(a[i + 1])
            elif a[i] == '-':
                rs -= int(a[i + 1])
            elif a[i] == '*':
                rs *= int(a[i + 1])
            i += 2

        return rs

    def opeartor_a_rs(self, a, opt, rs):
        if opt == '*':
            return map(lambda x: int(x) * int(a), rs)
        elif opt == '+':
            return map(lambda x: int(x) * int(a), rs)
        else:
            return map(lambda x: int(a) - int(x), rs)

    def compute_reminder_array(self, reminder):
        rs = []
        if len(reminder) == 1:
            return [int(reminder[0])]
        for i in range(0, len(reminder), 2):
            a = reminder[0: i + 1]
            if len(a) == len(reminder):
                # rs.extend([self.calc_str(a)])
                break
            opt = reminder[i + 1]
            rs.extend(self.opeartor_a_rs(self.calc_str(a), opt, self.compute_reminder_array(reminder[i + 2:])))
        return rs

    def to_array(self, input):
        a_input = list(input)
        operator = []
        for i in range(0, len(a_input)):
            if a_input[i] in ('+', '-', '*'):
                operator.append(a_input[i])
                a_input[i] = ','

        x = ''.join(a_input).split(',')
        a_input = [x[0]]
        i, j = 0, 1
        while i < len(operator) and j < len(x):
            a_input.append(operator[i])
            a_input.append(x[j])
            i += 1
            j += 1
        return a_input


s = Solution()
print(s.diffWaysToCompute("1-1"))
print(s.diffWaysToCompute("2-1-1"))
print(s.diffWaysToCompute("2*3-4*5"))
