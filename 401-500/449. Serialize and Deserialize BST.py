# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""

        return "(" + str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right) + ")"

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        root_str = data[1:len(data) - 1]
        root_val = root_str.split(",")[0]
        sub_str = root_str[len(root_val) + 1:]
        root = TreeNode(int(root_val))
        if len(sub_str) == 0:
            return root

        i, pattern = 1, 1
        while pattern != 0:
            i += 1
            if sub_str[i] == "(":
                pattern += 1
            if sub_str[i] == ")":
                pattern -= 1

        left = sub_str[0:i+1]
        right = sub_str[i+2:]

        root.left = self.deserialize(left)
        root.right = self.deserialize(right)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    s = Codec()
    encode = s.serialize(
        TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, right=TreeNode(1))),
                 TreeNode(-3, right=TreeNode(11))))
    print(encode)

    print(s.deserialize(encode))
