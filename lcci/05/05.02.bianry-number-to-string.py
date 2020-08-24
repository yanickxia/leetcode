class Solution:
    def printBin(self, num: float) -> str:
        res, i = "0.", 30
        while num > 0 and i:
            num *= 2
            if num >= 1:
                res += '1'
                num -= 1
            else:
                res += '0'
            i -= 1
        return res if not num else "ERROR"
