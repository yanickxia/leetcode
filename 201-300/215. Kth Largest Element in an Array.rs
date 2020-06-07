pub struct Solution;

// 堆排序是一个解决思路
// 快速选择，基于 QuickSoft 进行变形
impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums.clone();
        nums.sort();

        return nums[nums.len() - (k as usize)]
    }
}

#[cfg(test)]
mod tests {
    use crate::*;

    #[test]
    fn it_works() {
        assert_eq!(Solution::find_kth_largest(vec![3, 2, 1, 5, 6, 4], 2), 5);
        assert_eq!(Solution::find_kth_largest(vec![3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4);
    }
}

