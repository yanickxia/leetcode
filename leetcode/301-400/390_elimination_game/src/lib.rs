#[cfg(test)]
mod tests {
    struct Solution {}

    impl Solution {
        pub fn last_remaining(n: i32) -> i32 {
            if n == 1 {
                return 1;
            }
            if n == 2 {
                return 2;
            }


            return Solution::left_to_right(1, n, 2).0;
        }

        fn left_to_right(head: i32, tail: i32, step: i32) -> (i32, i32, i32) {
            let new_head = head + (step / 2);
            let new_tail = if (tail - head) % step != 0 { tail } else { tail - (step / 2) };

            if new_tail <= new_head {
                return (new_head, 0, 0);
            }

            return Solution::right_to_left(new_head, new_tail, step * 2);
        }

        fn right_to_left(head: i32, tail: i32, step: i32) -> (i32, i32, i32) {
            let new_head = if (tail - head) % step != 0 { head } else { head + (step / 2) };
            let new_tail = tail - (step / 2);
            if new_tail <= new_head {
                return (new_tail, 0, 0);
            }

            return Solution::left_to_right(new_head, new_tail, step * 2);
        }
    }

    #[test]
    fn it_works() {
        assert_eq!(6, Solution::last_remaining(16));
        assert_eq!(8, Solution::last_remaining(10));
        assert_eq!(2, Solution::last_remaining(3));
        assert_eq!(6, Solution::last_remaining(9));
        assert_eq!(4, Solution::last_remaining(7));
        assert_eq!(6, Solution::last_remaining(8));
        assert_eq!(1, Solution::last_remaining(1));
    }
}
