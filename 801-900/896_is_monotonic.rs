 
pub struct Solution {}

impl Solution {
    pub fn is_monotonic(a: Vec<i32>) -> bool {
        if a.len() <= 2 {
            return true;
        }
        let mut is_found_pattern = (false, false);

        for i in 1..a.len() {
            if !is_found_pattern.0 {
                if a[i - 1] != a[i] {
                    if a[i - 1] < a[i] {
                        is_found_pattern = (true, true)
                    } else {
                        is_found_pattern = (true, false)
                    }
                }
            } else {
                if is_found_pattern.1 && a[i - 1] > a[i] {
                    return false;
                } else if !is_found_pattern.1 && a[i - 1] < a[i] {
                    return false;
                }
            }
        }
        return true;
    }
}

#[cfg(test)]
mod tests {
    use crate::*;

    #[test]
    fn it_works() {
        assert_eq!(Solution::is_monotonic(vec![1, 2, 2, 4]), true);
        assert_eq!(Solution::is_monotonic(vec![1, 2, 5, 4]), false);
        assert_eq!(Solution::is_monotonic(vec![1, 1, 0]), true);
    }
}

