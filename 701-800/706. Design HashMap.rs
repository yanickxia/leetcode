struct MyHashMap {
    inner: Vec<Option<i32>>
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashMap {
    /** Initialize your data structure here. */
    fn new() -> Self {
        MyHashMap { inner: vec![Option::None; 1000000] }
    }

    /** value will always be non-negative. */
    fn put(&mut self, key: i32, value: i32) {
        self.inner[key as usize] = Option::Some(value)
    }

    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    fn get(&self, key: i32) -> i32 {
        match self.inner[key as usize] {
            Some(x) => {
                x
            }
            None => {
                -1
            }
        }
    }

    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    fn remove(&mut self, key: i32) {
        self.inner[key as usize] = Option::None
    }
}


#[cfg(test)]
mod tests {
    use crate::*;

    #[test]
    fn it_works() {}
}


