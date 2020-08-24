# 10 min
class Solution:
    def reverseBits(self, num: int) -> int:
        bin_num = bin(num)[2:]
        spited = []
        i = 0

        while i < len(bin_num):
            if bin_num[i] == "1":
                j = i + 1
                while j < len(bin_num) and bin_num[j] == "1":
                    j += 1
                spited.append(j - i)
                i = j
                continue
            i += 1
            spited.append(0)

        if len(spited) == 1:
            return spited[0] + 1

        for i in range(len(spited) - 1):
            if i + 2 < len(spited) and spited[i + 1] == 0 and spited[i + 2] != 0:
                spited[i] += 1 + spited[i + 2]
            elif spited[i + 1] == 0:
                spited[i] += 1

        return max(spited)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(1775))
    print(s.reverseBits(7))
