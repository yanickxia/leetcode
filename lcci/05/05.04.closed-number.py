from typing import List


class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        large = num + 1
        small = num -1
        n =  bin(num).count('1')
        while bin(large).count('1') != n and large <= 2147483647:
            large += 1
        while bin(small).count('1') != n and small >= 1:
            small -= 1

        large = large if bin(large).count('1') == n else -1
        small = small if bin(small).count('1') == n else -1

        return [large, small]


if __name__ == '__main__':
    s = Solution()

    print(s.findClosedNumbers(329246886))
    # [1156403407,1156403389]
    print(s.findClosedNumbers(1156403390))

    #  [571603726,571603696]
    print(s.findClosedNumbers(571603719))
    print(s.findClosedNumbers(17))
    print(s.findClosedNumbers(2))

    print(s.findClosedNumbers(1837591841))

    print(s.findClosedNumbers(1))
