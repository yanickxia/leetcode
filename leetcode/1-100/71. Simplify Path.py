# -*- coding:utf-8 -*-

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        i = 0
        res = ''
        while i < len(path):
            end = i + 1
            while end < len(path) and path[end] != "/":
                end += 1
            sub = path[i + 1:end]
            if len(sub) > 0:
                if sub == "..":
                    if stack != []: stack.pop()
                elif sub != ".":
                    stack.append(sub)
            i = end
        if stack == []: return "/"
        for i in stack:
            res += "/" + i
        return res


s = Solution()
print(s.simplifyPath("/../"))
print(s.simplifyPath("/."))
print(s.simplifyPath("/a/./b/../../c/"))
print(s.simplifyPath("/home/"))

print(s.simplifyPath("/..hidden"))
