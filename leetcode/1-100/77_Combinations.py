# -*- coding:utf-8 -*-
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []

        init_array = [[x] for x in range(1, n + 1)]
        return self.__combine(init_array, n, k - 1)

    def __combine(self, array, n, k):
        if k == 0:
            return array
        new_array = []
        for x in array:
            if x[-1] < n:
                i = x[-1]
                while i < n:
                    i += 1
                    n_a = list(x)
                    n_a.append(i)
                    new_array.append(n_a)
        return self.__combine(new_array, n, k - 1)


s = Solution()
print(s.combine(4, 2))
