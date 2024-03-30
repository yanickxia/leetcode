from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        pointers = {}
        max_block = sum(wall[0])
        for w in wall:
            cur = 0
            for i in w:
                cur += i
                if cur not in pointers:
                    pointers[cur] = 1
                else:
                    pointers[cur] += 1
        del pointers[max_block]
        if len(pointers) == 0:
            return len(wall)

        return len(wall) - max(pointers.values())



if __name__ == '__main__':
    s = Solution()

    print(s.leastBricks([[1, 1], [2], [1, 1]]))
    print(s.leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]) == 2)
    print(s.leastBricks([[100000000], [100000000], [100000000]]) == 3)
