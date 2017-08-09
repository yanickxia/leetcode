package leetcode;

import java.util.ArrayList;
import java.util.List;

public class SameTree {

	boolean flag = true;

	public boolean isSameTree(TreeNode p, TreeNode q) {

		List<TreeNode> pNodes = new ArrayList<TreeNode>();
		List<TreeNode> qNodes = new ArrayList<TreeNode>();
		pNodes = getNodes(p, pNodes);
		qNodes = getNodes(q, qNodes);

		if (pNodes.size() != qNodes.size())
			return false;
		for (int i = 0; i < pNodes.size(); i++) {
			TreeNode nP = pNodes.get(i);
			TreeNode nQ = qNodes.get(i);

			if ((nP != null && nQ == null) || (nP == null && nQ != null))
				return false;
			else if (nP != null && nQ != null) {
				if (pNodes.get(i).val != qNodes.get(i).val)
					return false;
			}

		}

		return true;

	}

	public List getNodes(TreeNode node, List lst) {

		if (node == null)
			return lst;
		if (node.left != null)
			getNodes(node.left, lst);
		else
			lst.add(null);

		if (node.right != null)
			getNodes(node.right, lst);
		else
			lst.add(null);

		lst.add(node);

		return lst;

	}

	public static void main(String[] args) {
		TreeNode t0 = new TreeNode(1);
		TreeNode t1 = new TreeNode(1);
		TreeNode t2 = new TreeNode(2);
		TreeNode t3 = new TreeNode(2);

		t0.left = t2;

		t1.left = null;
		t1.right = t3;

		System.out.println(new SameTree().isSameTree(t0, t1));

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