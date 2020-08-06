# 第一题. 字节跳动在北京有N个工区，形成一个环状，Bytebus是往返在各个工区的通勤车，按工区的顺序行驶，
# 其中第 i 个工区有汽油 gas[i] 升。你有一辆油箱容量无限的的Bytebus，
# 从第 i 个工区开往第 i+1 个工区需要消耗汽油 cost[i] 升。
# 你从其中的一个工区出发，开始时油箱为空。如果你可以绕环路行驶一周，则返回出发时工区的编号，否则返回 -1。


class Solution:
    def calc(self, gas, cost):
        less_funr = 0
        all_funr = 0

        begin = 0
        for i in range(len(gas)):
            begin = i
            all_funr += gas[i] - cost[i]
            if all_funr < 0:
                less_funr += all_funr
                all_funr = 0
                continue

        if all_funr + less_funr >=0:
            return begin
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.calc([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
