pub struct Solution {}

impl Solution {
    pub fn advantage_count(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let mut raw_b = b.clone();
        let mut a = a.clone();
        let mut b = b.clone();
        let mut resust = raw_b.clone();
        a.sort();
        b.sort();

        let mut remind_i = vec![];
        let mut fill_i = vec![];
        for i in 0..a.len() {
            fill_i.push(1)
        }

        let mut j = 0;
        for i in 0..a.len() {
            if a[i] > b[j] {
                let j_replace_index = raw_b.iter().position(|it| it == &b[j]).unwrap();
                resust[j_replace_index] = a[i];
                raw_b[j_replace_index] = -1;
                fill_i[j_replace_index] = -1;
                j += 1;
            } else {
                remind_i.push(a[i]);
            }
        }

        let mut x = 0;
        for i in 0..a.len() {
            if fill_i[i] != -1 {
                resust[i] = remind_i[x];
                x += 1;
            }
        }

        return resust;
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * let obj = WordFilter::new(words);
 * let ret_1: i32 = obj.f(prefix, suffix);
 */
#[cfg(test)]
mod tests {
    use crate::*;

    #[test]
    fn it_works() {
        assert_eq!(Solution::advantage_count(vec![2, 0, 4, 1, 2], vec![1, 3, 0, 0, 2]), vec![2, 0, 2, 1, 4]);
        assert_eq!(Solution::advantage_count(vec![12, 24, 8, 32], vec![13, 25, 32, 11]), vec![24, 32, 8, 12]);
        assert_eq!(Solution::advantage_count(vec![2, 7, 11, 15], vec![1, 10, 4, 11]), vec![2, 11, 7, 15]);
    }
}

