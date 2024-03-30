# -*- coding:utf-8 -*-

# todo 这里想要优化的话，第一不需要重新构建顺序数组，用i记住需要走的即可
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for i in range(0, len(gas)):
            if Solution.canFromBeginToEndCircuit(gas, cost):
                return i

            t_gas = gas[0]
            gas = gas[1:]
            gas.append(t_gas)

            t_cost = cost[0]
            cost = cost[1:]
            cost.append(t_cost)

        return -1

    @staticmethod
    def canFromBeginToEndCircuit(gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: bool
        """
        current_gas = gas[0]

        for i in range(0, len(gas)):
            current_gas -= cost[i]
            if current_gas < 0:
                return False
            if i < len(gas) - 1:
                current_gas += gas[i + 1]

        return True


if __name__ == '__main__':
    s = Solution()
    print s.canCompleteCircuit([2, 3, 4], [3, 4, 3])
    print s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
