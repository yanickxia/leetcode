impl Solution {
    pub fn max_power(s: String) -> i32 {
        let s = s.chars().collect::<Vec<char>>();
        let mut max = 0;
        for mut i in 0..s.len() {
            let mut current = 0;
            for j in 0..(s.len() - i) {
                if s[i] == s[i + j] {
                    current += 1;
                    if current > max {
                        max = current
                    }
                } else {
                    i += current;
                    break;
                }
            }
        }

        return max as i32;
    }
}
