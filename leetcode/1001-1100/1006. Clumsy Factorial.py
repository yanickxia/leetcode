class Solution:
    def clumsy(self, N: int) -> int:
        opt = 0
        q1 = []
        for i in range(N, 0, -1):
            q1.append(i)
            if i == 1:
                break
            if opt == 0:
                q1.append("*")
            elif opt == 1:
                q1.append("/")
            elif opt == 2:
                q1.append("+")
            else:
                q1.append("-")
            opt += 1
            if opt == 4:
                opt = 0

        for i in range(0, len(q1)):
            if q1[i] == "*":
                q1[i + 1] = q1[i - 1] * q1[i + 1]
                q1[i - 1] = "null"
                q1[i] = "null"
            elif q1[i] == "/":
                q1[i + 1] = int(q1[i - 1] / q1[i + 1])
                q1[i - 1] = "null"
                q1[i] = "null"

        q1 = [x for x in q1 if x != "null"]
        for i in range(0, len(q1)):
            if q1[i] == "+":
                q1[i + 1] = q1[i - 1] + q1[i + 1]
            elif q1[i] == "-":
                q1[i + 1] = q1[i - 1] - q1[i + 1]

        return q1[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.clumsy(10))
    print(s.clumsy(4))
