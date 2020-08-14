class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # 去除首尾空格

        isDot, isDigit, isE = False, False, False  # 点，数字，e

        for i, x in enumerate(s):
            if x == "e":
                if not isDigit or isE:  # 前面没有数字，or 前面已经存在字符 e
                    return False

                isDigit = False  # 设置isDigit = false
                isE = True
            elif x in "+-":
                if i != 0 and s[i - 1] != "e":  # +- 只能出现首位，和 字符e的后面
                    return False
            elif x == ".":
                if isDot or isE:  # 字符 .（小数点）只能出现一次，而且是只能出现在 e 的前面
                    return False
                isDot = True
            elif x.isdecimal():  # 检查字符串是否只包含十进制字符
                isDigit = True
            else:
                return False

        return len(s) > 0 and isDigit

if __name__ == '__main__':
    s = Solution()
    print(s.isNumber("0") == True)
    print(s.isNumber('.') == False)
    print(s.isNumber('.5') == True)
    print(s.isNumber(" ") == False)

    print(s.isNumber("abc") == False)
    print(s.isNumber("2e10") == True)
    print(s.isNumber("1 a") == False)
    print(s.isNumber(" -90e3   ") == True)
    print(s.isNumber("e3") == False)
    print(s.isNumber(" 6e-1") == True)
    print(s.isNumber("-+3") == False)
    print(s.isNumber('e') == False)
    print(s.isNumber("95a54e53") == False)
    print(s.isNumber("99e2.5") == False)
    print(s.isNumber(" --6 ") == False)
    print(s.isNumber("0e") == False)