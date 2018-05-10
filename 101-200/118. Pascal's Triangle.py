class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []
        rs = []
        rs.append([1])
        if numRows == 1:
            return rs
        rs.append([1, 1])
        if numRows == 2:
            return rs

        i = numRows - 2
        while i > 0:
            latest_nums = rs[-1]
            ts = []
            for j in range(0, len(latest_nums) - 1):
                ts.append(latest_nums[j] + latest_nums[j + 1])
            ts = [1] + ts + [1]
            rs.append(ts)
            i -= 1
        return rs

s = Solution()
print(s.generate(5))
