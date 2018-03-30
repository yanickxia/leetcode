# -*- coding:utf-8 -*-

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        input_list = ["(" + input + ")"]
        real_rs_list = []
        real_rs_list.extend(input_list)

        for x in input_list:
            x_list = list(x)
            for i in range(1, len(x_list)):
                if x_list[i].isdigit():
                    an_list = list(x_list)
                    an_list.insert(i, '(')
                    new_x = ''.join(an_list)
                    new_rs = Solution.insert_a_right_pathness(new_x)
                    real_rs_list.extend(new_rs)
                    input_list = new_rs
        new_real_rs_list = []
        for x in real_rs_list:
            is_need = True
            for i in range(0, len(x) - 2):
                if x[i] == '(' and x[i + 2] == ')':
                    is_need = False

            if is_need:
                new_real_rs_list.append(x)

        real_rs_list = [eval(item) for item in new_real_rs_list]

        return real_rs_list

    @staticmethod
    def insert_a_right_pathness(str_n):
        a_list = list(str_n)
        rs = []
        for x in range(0, len(a_list)):
            if a_list[x].isdigit():
                if x > 1 and a_list[x - 2] == '(':
                    continue
                t_list = list(a_list)
                t_list.insert(x + 1, ')')
                rs.append(''.join(t_list))
        return rs[0:len(rs) - 1]


s = Solution()
print(s.diffWaysToCompute("2*3-4*5"))
