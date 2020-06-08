use std::cmp::max;

pub struct Solution {}

impl Solution {
    pub fn predict_the_winner(piles: Vec<i32>) -> bool {
        return Solution::stone_game_goal(&piles) >= 0;
    }

    fn stone_game_goal(piles: &[i32]) -> i32 {
        let n = piles.len();
        let mut dp = vec![vec![0; n]; n];

        // 当i==j时，取得的在i-j范围内，最大值即为nums[i]；
        for i in 0..n {
            dp[i][i] = piles[i];
        }

        for end in 1..n {
            let mut i = 0;
            let mut j = end;
            while j < n {
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1]);
                i += 1;
                j += 1;
            }
        }

        return dp[0][n - 1];
    }
}

#[cfg(test)]
mod tests {
    use crate::*;

    #[test]
    fn it_works() {
        assert_eq!(Solution::predict_the_winner(vec![5, 3, 4, 5]), true);
        assert_eq!(Solution::predict_the_winner(vec![7, 7, 12, 16, 41, 48, 41, 48, 11, 9, 34, 2, 44, 30, 27, 12, 11, 39, 31, 8, 23, 11, 47, 25, 15, 23, 4, 17, 11, 50, 16, 50, 38, 34, 48, 27, 16, 24, 22, 48, 50, 10, 26, 27, 9, 43, 13, 42, 46, 24]), true);
    }
}

