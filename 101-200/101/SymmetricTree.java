package info.yannxia.java.leetcode;

import java.util.ArrayList;
import java.util.List;

public class SymmetricTree {

    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }


        return checkNode(root.left, root.right);
    }

    private boolean checkNode(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        }
        if (left == null || right == null) {
            return false;
        }
        if (left.val != right.val) {
            return false;
        }

        return checkNode(left.left, right.right)
                && checkNode(left.right, right.left);
    }

}


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}
