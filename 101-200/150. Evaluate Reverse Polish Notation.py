from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for e in tokens:
            if e in ['+', '-', '*', '/']:
                denominator = int(stack.pop())
                nominator = int(stack.pop())
                if e == '+':
                    stack.append(nominator + denominator)
                elif e == '-':
                    stack.append(nominator - denominator)
                elif e == '*':
                    stack.append(nominator * denominator)
                else:
                    tmp = -(-nominator // denominator) if (nominator < 0) ^ (denominator < 0) else nominator // denominator
                    stack.append(tmp)
            else:
                stack.append(e)
        return stack.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["4", "-2", "/", "2", "-3", "-", "-"]))
    print(s.evalRPN(["2", "1", "+", "3", "*"]))
    print(s.evalRPN(["4", "13", "5", "/", "+"]))
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
