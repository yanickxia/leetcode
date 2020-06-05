#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::rc::Rc;
use std::cell::RefCell;

pub struct Solution {}

impl Solution {
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if preorder.len() == 1 && inorder.len() == 1 {
            return Option::Some(Rc::new(RefCell::new(TreeNode::new(preorder[0]))));
        }
        if preorder.len() == 0 && inorder.len() == 0 {
            return Option::None;
        }

        let root = preorder[0];
        let mut split = inorder.split(|x| x.eq(&root));
        let left = split.next().unwrap();
        let right = split.next().unwrap();

        let preorder_left = &preorder[1..left.len() + 1];
        let preorder_right = &preorder[left.len() + 1..];

        let mut rootNode = Rc::new(RefCell::new(TreeNode::new(root)));
        rootNode.borrow_mut().left = Solution::build_tree(preorder_left.to_owned(), Vec::from(left));
        rootNode.borrow_mut().right = Solution::build_tree(preorder_right.to_owned(), Vec::from(right));

        return Option::Some(rootNode);
    }
} 
