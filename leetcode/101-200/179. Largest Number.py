from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        nums = sorted(nums, key=cmp_to_key(Solution.cmp), reverse=True)
        # max_len = max([len(x) for x in nums])
        # weight = []
        #
        # for n in nums:
        #     w = n
        #     while len(w) < max_len:
        #         if max_len - len(w) > len(w):
        #             w = n.ljust(max_len, w)
        #         else:
        #             w = n.ljust(max_len, w[0:max_len - len(w)])
        #
        #     weight.append(w)
        #
        # new_nums_with_key = []
        # for i in range(len(nums)):
        #     new_nums_with_key.append((nums[i], weight[i]))
        #
        # new_nums_with_key = sorted(new_nums_with_key, key=lambda x: x[1], reverse=True)
        #
        return str(int(''.join(nums)))

    @staticmethod
    def find_bigger_num(nums: List[int]):
        pass

    @staticmethod
    def cmp(x, y):
        if x + y > y + x:
            return 1
        elif x+y == y+x:
            return 0
        else:
            return -1


if __name__ == '__main__':
    s = Solution()

    print(s.largestNumber([121, 12]) == "12121")
    print(s.largestNumber([824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247]) == "9609938824824769735703560743981399")
    print(s.largestNumber([3, 30, 34, 5, 9]))
    print(s.largestNumber([0, 0]))
