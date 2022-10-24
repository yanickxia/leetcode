# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

# time cost: 17 min
class Solution:
    class Item:
        content = ""
        path = ""

        def __init__(self, content, path):
            self.content = content
            self.path = path

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        all_contents = {}

        for i in range(0, len(paths)):
            parsed = Solution.parse(paths[i])
            for j in range(0,len(parsed)):
                if parsed[j].content not in all_contents:
                    all_contents[parsed[j].content] = [parsed[j].path]
                else:
                    all_contents[parsed[j].content].append(parsed[j].path)
        ans = []
        for k,v in all_contents.items():
            if len(v) > 1:
                ans.append(v)
        return ans

    @staticmethod
    def parse(path_string: str):
        spilted = path_string.split(" ")
        path = spilted[0]
        items = []
        for i in spilted[1:]:
            filename = i[0:i.index("(")]
            content = i[i.index("(") + 1:len(i) - 1]
            items.append(Solution.Item(content, path + "/" + filename))

        return items


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])