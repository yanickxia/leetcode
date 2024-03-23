from collections import deque, defaultdict
from typing import List


# 解体思路，只有一个单向的 LIST 才能完成，无论是分段还是环了，都无法完成，因此用 LinkedList 显然特别好解决这个问题
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.best_canFinish(numCourses, prerequisites)

        prerequisites_map = {}
        can_reach = set()
        for prerequisite in prerequisites:
            a, b = prerequisite[0], prerequisite[1]
            if a == b:
                return False
            if a not in prerequisites_map:
                prerequisites_map[a] = []
            prerequisites_map[a].append(b)

        for prerequisite in prerequisites:
            a, b = prerequisite[0], prerequisite[1]
            if b in can_reach:
                continue
            if self.check_can_finsih(prerequisites_map, b, can_reach, set()) is False:
                return False
            can_reach.add(b)

        return True

    def check_can_finsih(self, prerequisites_map, b: int, can_reach, visited):
        if b not in prerequisites_map:
            can_reach.add(b)
            return True
        if b in can_reach:
            return True

        if b in visited:
            return False

        if b in prerequisites_map:
            visited.add(b)
            all_req = prerequisites_map[b]
            for x in all_req:
                if self.check_can_finsih(prerequisites_map, x, can_reach, visited) is False:
                    return False
                can_reach.add(x)
        return True

    from collections import defaultdict, deque

    def best_canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Create an adjacency list to represent the directed graph
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # Step 2: Create an array "indegrees" to store the number of incoming edges for each node in the graph
        indegrees = [0] * numCourses
        for prereq, _ in prerequisites:
            indegrees[prereq] += 1

        # Step 3: Add all the nodes with indegree 0 to a queue
        queue = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)

        # Step 4: Topological Sort
        while queue:
            course = queue.popleft()
            for prereq in graph[course]:
                indegrees[prereq] -= 1
                if indegrees[prereq] == 0:
                    queue.append(prereq)

        # Step 5: Check if we have removed all the courses successfully
        return all(indegree == 0 for indegree in indegrees)


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]))
    print(s.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]) == True)
    print(s.canFinish(3, [[1, 0], [2, 0], [0, 2]]) == False)
    print(s.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
    print(s.canFinish(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]) == False)
    print(s.canFinish(2, [[1, 0], [0, 1]]) == False)
    print(s.canFinish(2, [[1, 0]]) == True)

####
