import unittest
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty_and_profit = []
        for i in range(len(difficulty)):
            difficulty_and_profit.append((difficulty[i], profit[i]))

        softed_difficulty_and_profit_by_difficulty = sorted(difficulty_and_profit, key=lambda x: x[0])
        difficulty = [x[0] for x in softed_difficulty_and_profit_by_difficulty]
        profit = [x[1] for x in softed_difficulty_and_profit_by_difficulty]
        worker = sorted(worker)

        less_n_max_profit = []
        current = 0
        for i in range(len(difficulty)):
            if profit[i] > current:
                current = profit[i]
            less_n_max_profit.append(current)

        difficulty = difficulty[::-1]
        less_n_max_profit = less_n_max_profit[::-1]
        worker = worker[::-1]

        result = 0
        for i in range(len(difficulty)):
            while len(worker) > 0 and worker[0] >= difficulty[i]:
                worker = worker[1:]
                result += less_n_max_profit[i]

        return result


class TestSolution(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]), 100)
        self.assertEqual(s.maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]), 0)


if __name__ == '__main__':
    unittest.main()
