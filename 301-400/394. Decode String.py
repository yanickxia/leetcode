class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 0:
            return ""

        pre, repeat_times, repeat_point_left, repeat_point_right = "", "", None, None
        for i in range(0, len(s)):
            if s[i].isalpha():
                pre += s[i]
            elif s[i].isdigit():
                repeat_times += s[i]
            else:
                # is [
                left, j = 1, i
                repeat_point_left = j
                while left != 0:
                    j += 1
                    if s[j] == "[":
                        left += 1
                    elif s[j] == "]":
                        left -= 1
                repeat_point_right = j
                break
        if len(repeat_times) == 0:
            return pre

        return pre + \
               (int(repeat_times) * self.decodeString(s[repeat_point_left + 1:repeat_point_right])) + \
               self.decodeString(s[repeat_point_right + 1:])


if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("3[a]2[bc]") == "aaabcbc")
    print(s.decodeString("3[a2[c]]") == "accaccacc")
    print(s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
    print(s.decodeString("abc3[cd]xyz") == "abccdcdcdxyz")
