struct Solution {}


impl Solution {
    pub fn min_cost_to_move_chips(chips: Vec<i32>) -> i32 {
        let even = chips.iter().map(|it| it % 2)
            .sum::<i32>();
        let odd = chips.len() as i32 - even;
        if even > odd {
            odd
        } else {
            even
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::*;

    #[test]
    fn it_works() {
        assert_eq!(Solution::min_cost_to_move_chips(vec![1, 2, 3]), 1);
        assert_eq!(Solution::min_cost_to_move_chips(vec![2, 2, 2, 3, 3]), 2);
    }
}


