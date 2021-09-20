impl Solution {
    pub fn reverse_words(s: String) -> String {
        return s.split_ascii_whitespace()
            .map(|x| x.chars().rev().collect::<String>())
            .collect::<Vec<String>>()
            .join(" ");
    }
}
