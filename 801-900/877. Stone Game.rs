use std::cmp::max;

pub struct Solution {}

impl Solution {
    pub fn stone_game(piles: Vec<i32>) -> bool {
        let result = piles.iter().sum::<i32>();
        let first = Solution::stone_game_goal(&piles);
        let remind = result - first;
        return first > remind;
    }

    fn stone_game_goal(piles: &[i32]) -> i32 {



        if piles.len() == 1 {
            return piles[0];
        }
        return max(piles[0] + Solution::stone_game_goal(Vec::from(&piles[1..])),
                   piles[piles.len() - 1] + Solution::stone_game_goal(Vec::from(&piles[0..piles.len() - 1])));
    }
}

#[cfg(test)]
mod tests {
    use crate::*;

    #[test]
    fn it_works() {
        assert_eq!(Solution::stone_game(vec![5, 3, 4, 5]), true);
        assert_eq!(Solution::stone_game(vec![7, 7, 12, 16, 41, 48, 41, 48, 11, 9, 34, 2, 44, 30, 27, 12, 11, 39, 31, 8, 23, 11, 47, 25, 15, 23, 4, 17, 11, 50, 16, 50, 38, 34, 48, 27, 16, 24, 22, 48, 50, 10, 26, 27, 9, 43, 13, 42, 46, 24]), true);
    }
}


