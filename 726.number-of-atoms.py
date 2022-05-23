#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#

# @lc code=start
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # remove invaild (
        cout = 0
        while formula[0] == "(" and formula[-1] == ")":
            formula = formula[1:len(formula)-1]

        newFormula = ""
        # one way for empty to 1
        for i in range(0, len(formula) - 1):
            if formula[i].isalpha() and ((formula[i + 1].isalpha() and formula[i + 1].isupper()) or (
                    formula[i + 1] == "(" or (formula[i + 1] == ")"))):
                newFormula += formula[i] + "1"
                continue
            if formula[i]== ")" and not formula[i+1].isnumeric():
                newFormula += formula[i]+"1"
                continue
            else:
                newFormula += formula[i]
        newFormula += formula[-1]
        if newFormula[-1].isalpha():
            newFormula += "1"

        formula = newFormula

        stack = []
        i = 0
        while i < len(formula):
            if formula[i].isalpha() and formula[i].isupper():
                key, offset = Solution.findNextAtom(formula, i)
                i += offset
                num, offset = Solution.findNextNum(formula, i)
                i += offset
                stack.append((key, num))
                continue
            if formula[i] == "(":
                stack.append("(")
                i += 1
                continue
            if formula[i] == ")":
                num, offset = Solution.findNextNum(formula, i + 1)
                i += offset + 1

                items = []
                item = stack.pop()
                while item != "(":
                    items.append((item[0], item[1] * num))
                    item = stack.pop()
                stack.extend(items)

        ans = {}
        for x in stack:
            if x[0] not in ans:
                ans[x[0]] = 0
            ans[x[0]]+=x[1]

        ansStr = ""
        keys = list(ans.keys())
        keys.sort()

        for k in keys:
            if ans[k] == 1:
                ansStr += k
            else:
                ansStr += k + str(ans[k])

        return ansStr

    @staticmethod
    def findNextNum(formula, begin):
        b = begin
        while b < len(formula) and formula[b].isnumeric():
            b += 1
        return int(formula[begin:b]), b - begin

    @staticmethod
    def findNextAtom(formula, begin):
        b = begin
        while b < len(formula) and formula[b].isalpha():
            b += 1
        return formula[begin:b], b - begin


# @lc code=end

if __name__ == '__main__':
    s = Solution()

    print(s.countOfAtoms("Mg((H2O)2Na)4(F)(H2SO4)N") == "FH18MgNNa4O12S")
    print(s.countOfAtoms("Mg(H2O)N"))
    print(s.countOfAtoms("(H)"))
    print(s.countOfAtoms("K4(ON(SO3)2)2"))
    print(s.countOfAtoms("HFe4"))
    print(s.countOfAtoms("H2O"))
    print(s.countOfAtoms("Mg(OH)2"))
