class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        reversed_n2 = num2[::-1]
        n_array = []
        zero_count = ""
        for n in reversed_n2:
            x = self.multiply_single(num1, int(n))
            n_array.append(x + zero_count)
            zero_count += "0"

        sum = "0"
        for n in n_array:
            sum = ''.join(str(e) for e in self.add_single(n, sum))

        while sum[0] == "0" and len(sum) > 1:
            sum = sum[1:len(sum)]
        return sum

    def add_single(self, n1, n2):
        max_n1 = len(n1)
        max_n2 = len(n2)
        if max_n1 > max_n1:
            n1 = n1.zfill(max_n2)
        else:
            n2 = n2.zfill(max_n1)
        carry = 0
        array = []
        for i in range(len(n1) - 1, -1, -1):
            x = int(n2[i]) + int(n1[i]) + carry
            carry = int(x / 10)
            array.append(str(x % 10))
        array.append(carry)

        return array[::-1]

    def multiply_single(self, num1, n):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        newN = ""
        for c in num1[::-1]:
            x = int(c) * n + carry
            carry = int(x / 10)
            mod = x % 10
            newN += str(mod)
        newN += str(carry)

        return newN[::-1]


s = Solution()

print(s.multiply("0", "0"))
print(s.multiply("999", "999"))
