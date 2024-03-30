from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stations = {}
        for i in range(0, len(routes)):
            for j in range(0, len(routes[i])):
                start = routes[i][j]
                if start not in stations:
                    stations[start] = set()
                station = stations.get(start)
                stations[start] = station.union(routes[i])
                stations[start].remove(start)
        if source not in stations or target not in stations:
            return -1
        if source == target:
            return 0
        queue, visited = [source], set()
        counter = 0
        while len(queue) > 0:
            counter += 1
            for i in range(0, len(queue)):
                station = queue.pop(0)
                for reach_station in stations[station]:
                    if reach_station in visited:
                        continue
                    visited.add(reach_station)
                    if reach_station == target:
                        return counter
                    queue.append(reach_station)
        return -1


if __name__ == '__main__':
    s = Solution()

    print(s.numBusesToDestination(
        [[10, 13, 22, 28, 32, 35, 43], [2, 11, 15, 25, 27], [6, 13, 18, 25, 42], [5, 6, 20, 27, 37, 47],
         [7, 11, 19, 23, 35], [7, 11, 17, 25, 31, 43, 46, 48], [1, 4, 10, 16, 25, 26, 46], [7, 11],
         [3, 9, 19, 20, 21, 24, 32, 45, 46, 49], [11, 41]], 37, 43) == 3)

    print(s.numBusesToDestination([[1, 7], [3, 5]], 5, 5) == 0)
    print(s.numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12) == -1)
    print(s.numBusesToDestination([[24], [3, 6, 11, 14, 22], [1, 23, 24], [0, 6, 14], [1, 3, 8, 11, 20]], 20, 8) == 1)
    print(s.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6) == 2)
    print(s.numBusesToDestination([[2], [2, 8]], 8, 2) == 1)
    # print(s.numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12))
