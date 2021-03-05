from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        min_cross = len(wall)
        raw_col = len(wall)

        while True:

            current_walls = []
            current_min = float("INF")

            wall = [x for x in wall if len(x) > 1]
            current_cross = len(wall)

            for i in range(0, len(wall)):
                current_wall = wall[i][0]
                if current_wall < current_min:
                    current_min = current_wall
                current_walls.append(current_wall)

            for j in range(0, len(current_walls)):
                replace = current_walls[j] - current_min
                if replace == 0:
                    current_cross -= 1
                    wall[j] = wall[j][1:]
                else:
                    wall[j][0] = replace

            if len(wall) == 0:
                return min_cross

            current_cross += (raw_col - len(wall))

            if current_cross < min_cross:
                min_cross = current_cross


if __name__ == '__main__':
    s = Solution()

    print(s.leastBricks([[1, 1], [2], [1, 1]]))
    print(s.leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]) == 2)
    print(s.leastBricks([[100000000], [100000000], [100000000]]) == 3)
