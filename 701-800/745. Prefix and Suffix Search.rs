use std::collections::HashMap;

struct WordFilter {
    vec: Vec<String>,
    key_with_index: Vec<(String, i32)>,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordFilter {
    fn new(words: Vec<String>) -> Self {
        let mut keys = HashMap::<String, i32>::new();
        let mut key_with_index = Vec::<(String, i32)>::new();

        for i in (0..words.len()).rev() {
            let word = &words[i];
            if !keys.contains_key(word) {
                keys.insert(word.to_string(), 0);
                key_with_index.push((word.to_string(), i as i32))
            }
        }

        WordFilter {
            vec: words.clone(),
            key_with_index,
        }
    }

    fn f(&self, prefix: String, suffix: String) -> i32 {
        for i in 0..self.key_with_index.len() {
            if self.key_with_index[i].0.starts_with(&prefix) &&
                self.key_with_index[i].0.ends_with(&suffix) {
                return self.key_with_index[i].1;
            }
        }

        return -1;
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
        let wf = WordFilter::new(vec!["apple".to_string()]);
        assert_eq!(wf.f("a".to_string(), "e".to_string()), 0)
    }
}

