import math


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        n_numbers = []
        for i in range(0, n):
            n_numbers.append(i + 1)

        if math.factorial(n) == k:
            return ''.join([str(x) for x in n_numbers])[::-1]

        return self.get_permutation(n_numbers, k-1)

    def get_permutation(self, n_numbers, k):
        if k == 0:
            return ''.join([str(x) for x in n_numbers])

        times = math.factorial((len(n_numbers) - 1))
        x = k / times
        leave_k = k - times * x
        this_n = n_numbers[x]
        del n_numbers[x]

        return str(this_n) + self.get_permutation(n_numbers, leave_k)


s = Solution()
print(s.getPermutation(1, 1))
print(s.getPermutation(2, 2))

print(s.getPermutation(3, 3))
print(s.getPermutation(3, 4))

print(s.getPermutation(4, 12))
