from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        count = 2
        array = [[0 for i in range(n)] for i in range(n)]
        i, j = 0, 1
        array[0][0] = 1
        direct = 0
        while True:
            if direct == 0:  # RIGHT
                while j < n and array[i][j] == 0:
                    array[i][j] = count
                    count += 1
                    j += 1
                direct = 1
            i += 1
            j -= 1
            if direct == 1:  # DOWN
                while i < n and array[i][j] == 0:
                    array[i][j] = count
                    count += 1
                    i += 1
                direct = 2
            i -= 1
            j -= 1
            if direct == 2:  # LEFT
                while j < n and array[i][j] == 0:
                    array[i][j] = count
                    count += 1
                    j -= 1
                direct = 3
            j += 1
            i -= 1

            if direct == 3:  # UP
                while i < n and array[i][j] == 0:
                    array[i][j] = count
                    count += 1
                    i -= 1
                direct = 0
            i += 1
            j += 1
            if count > n * n:
                break

        return array


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
    print(s.generateMatrix(4))
