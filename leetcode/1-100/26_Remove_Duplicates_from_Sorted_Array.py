# -*- coding:utf-8 -*-


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        j = 0
        for i in range(0, len(A)):
            if A[i] != A[j]:
                A[i], A[j + 1] = A[j + 1], A[i]
                j = j + 1
        return j + 1


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))
    print(s.removeDuplicates([]))
