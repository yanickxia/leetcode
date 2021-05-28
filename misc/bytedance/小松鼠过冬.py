class Solution:
    def calc(self, input):
        ave = sum(input) / (len(input))
        diff = 0
        latest = 0
        count = 0
        for i in range(len(input)):
            diff += input[i] - ave
            if diff == 0:
                count += i - latest
                latest = i
        if len(input) - 1 != latest:
            count += (len(input)) - latest
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.calc([9, 9, 15, 7]))
