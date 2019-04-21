# -*- coding:utf-8 -*-

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        res_map = {}
        res_array = []
        for i in range(len(nums)):
            num = nums[i]
            for item in num:
                if item not in res_map:
                    res_map[item] = NumberIndex(item, i)
                else:
                    res_map[item].index.add(i)

        for key in sorted(res_map.keys()):
            res_array.append(res_map[key])

        # find minimum range in appear array
        i, k = 0, len(nums)
        result = (res_array[0].num, res_array[-1].num)
        while i < len(res_array):
            find_diereses = set()
            j = i
            while len(find_diereses) != k:
                if j == len(res_array):
                    break
                find_diereses = find_diereses.union(res_array[j].index)

                if len(find_diereses) == k:
                    break
                j += 1
            if len(find_diereses) == k:
                # print res_array[i].num, res_array[j].num
                if (res_array[j].num - res_array[i].num) < (result[1] - result[0]):
                    result = (res_array[i].num, res_array[j].num)
            i += 1

        return result


class NumberIndex():
    def __init__(self, x, first_row):
        self.num = x
        self.index = set()
        self.index.add(first_row)


if __name__ == '__main__':
    s = Solution()
    print s.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
    print s.smallestRange([[1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 10]])
    print s.smallestRange(
        [[24, 25, 26, 31, 33], [-27, -26, 37, 40, 72, 79, 83, 88, 92, 92, 92, 93], [33, 81, 83, 87, 87, 94],
         [-53, -23, -15, 11, 37, 44], [-40, 7, 7, 11], [-42, -3, 4, 7, 8, 8, 11], [19, 30, 44, 49, 50],
         [-5, 29, 31, 32, 32, 36], [25, 30, 31, 32, 32, 34, 34, 35], [1, 3, 10, 15, 15, 16], [1, 7, 13, 13, 21],
         [-15, -6, -6, -5, 5, 6, 10], [76, 77, 81, 83, 83, 85, 85, 85, 85, 85, 85, 86], [-59, -49, 18], [70, 71],
         [-9, 45, 46, 48, 49], [8, 42, 48, 54, 55, 58]])
