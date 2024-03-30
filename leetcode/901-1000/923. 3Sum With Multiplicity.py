import collections
from typing import List


class Solution(object):
    def threeSumMulti(self, A: List[int], target: int) -> int:
        cnt = collections.Counter(A)
        keys = sorted(cnt)
        s = 0
        for i, ki in enumerate(keys):
            n = cnt[ki]
            if ki > target:
                break
            elif 3 * ki == target:  # case A[i] == A[j] == A[k]
                s += n * (n - 1) * (n - 2) // 6 if n >= 3 else 0  # combination Cr(n, 3)
            elif target - 2 * ki in keys:  # case A[i] == A[j] != A[k] or A[i] != A[j] == A[k]
                s += cnt[target - 2 * ki] * n * (n - 1) // 2 if n >= 2 else 0  # combination Cr(n, 2)
            for j, kj in enumerate(keys[i + 1:], i + 1):
                num = target - ki - kj
                if num < 0:
                    break
                elif num in keys[j + 1:]:  # case A[i] != A[j] != A[k]
                    s += n * cnt[kj] * cnt[num]
        return s % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))
    print(s.threeSumMulti([1, 1, 2, 2, 2, 2], 5))
