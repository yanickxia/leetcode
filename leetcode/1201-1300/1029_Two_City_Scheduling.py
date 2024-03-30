from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund = []
        N = len(costs) // 2
        minCost = 0
        for A, B in costs:
            refund.append(B - A)
            minCost += A
        refund.sort()
        for i in range(N):
            minCost += refund[i]
        return minCost


if __name__ == '__main__':
    s = Solution()
    print(s.twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]), 1859)
    print(s.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]), 110)
    print(s.twoCitySchedCost([[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]), 3086)
