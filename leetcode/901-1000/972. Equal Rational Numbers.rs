pub struct Solution {}

impl Solution {
    pub fn is_rational_equal(s: String, t: String) -> bool {
        if !s.contains("(") && !t.contains("(") {
            return &format!("{:0<5}", s.replace(".", "")) == &format!("{:0<5}", t.replace(".", ""));
        }

        let s_split = s.split(".").collect::<Vec<&str>>();
        let t_split = t.split(".").collect::<Vec<&str>>();
        let s_integer = s_split[0];
        let t_integer = t_split[0];

        let mut s_non_rep: &str = "0";
        let mut s_rep: &str = "0";
        if s_split.len() > 1 {
            let s_non_rep_and_re = s_split[1].split("(").collect::<Vec<&str>>();
            s_non_rep = s_non_rep_and_re[0];
            if s_non_rep_and_re.len() > 1 {
                s_rep = &s_non_rep_and_re[1][0..s_non_rep_and_re[1].len() - 1];
            }
        }

        let mut t_non_rep: &str = "0";
        let mut t_rep: &str = "0";
        if t_split.len() > 1 {
            let t_non_rep_and_re = t_split[1].split("(").collect::<Vec<&str>>();
            t_non_rep = t_non_rep_and_re[0];
            if t_non_rep_and_re.len() > 1 {
                t_rep = &t_non_rep_and_re[1][0..t_non_rep_and_re[1].len() - 1];
            }
        }


        let mut nth_loop = false;
        let mut s_num = 0;
        //for 0.999999...
        if s_rep.eq("9") || s_rep.eq("99") || s_rep.eq("999") || s_rep.eq("9999") {
            nth_loop = true;
            s_num = (s_integer.to_string() + &format!("{:9<5}", s_non_rep)).parse().unwrap();
            s_num += 1;
        } else {
            s_num = (s_integer.to_string() + &format!("{:0<5}", s_non_rep)).parse().unwrap();
        }
        let mut t_num = -1;
        if t_rep.eq("9") || t_rep.eq("99") || t_rep.eq("999") || t_rep.eq("9999") {
            nth_loop = true;
            t_num = (t_integer.to_string() + &format!("{:9<5}", t_non_rep)).parse().unwrap();
            t_num += 1;
        } else {
            t_num = (t_integer.to_string() + &format!("{:0<5}", t_non_rep)).parse().unwrap();
        }

        if nth_loop && s_num == t_num {
            return true;
        }


        // for 0.(52) == 0.(52)
        if s_integer == t_integer && s_non_rep == t_non_rep && s_rep == t_rep {
            return true;
        }

        // for 0.1(6) == 0.1(66) |  0.1(33) == 0.1(333)
        if t_non_rep == s_non_rep {
            return s_rep.to_string().repeat(t_rep.len()) == t_rep.to_string().repeat(s_rep.len());
        }

        //for  S = "0.(52)", T = "0.5(25)"
        let mut less_non_rep;
        let mut bigger_non_rep;
        let mut less_rep;
        let mut bigger_rep;
        if s_non_rep > t_non_rep {
            less_non_rep = t_non_rep.to_string();
            less_rep = t_rep.to_string();
            bigger_non_rep = s_non_rep.to_string();
            bigger_rep = s_rep.to_string();
        } else {
            less_non_rep = s_non_rep.to_string();
            less_rep = s_rep.to_string();
            bigger_non_rep = t_non_rep.to_string();
            bigger_rep = t_rep.to_string();
        }


        for i in 0..(bigger_non_rep.len() - less_non_rep.len()) {
            less_non_rep = less_non_rep + &less_rep[0..1];
            less_rep = (&less_rep[1..less_rep.len()]).to_string() + &less_rep[0..1];
            if (less_rep == bigger_rep || bigger_rep.starts_with(&less_rep) || less_rep.starts_with(&bigger_rep)) && (less_non_rep == bigger_non_rep) {
                return true;
            }
        }


        return false;
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
        assert_eq!(Solution::is_rational_equal("3434.3434(3434)".to_string(), "3434.34(34)".to_string()), true);
        assert_eq!(Solution::is_rational_equal("1414.1414(14)".to_string(), "1414.14(1414)".to_string()), true);
        assert_eq!(Solution::is_rational_equal("1".to_string(), "0.99(99)".to_string()), true);
        assert_eq!(Solution::is_rational_equal("0.(0)".to_string(), "0".to_string()), true);
        assert_eq!(Solution::is_rational_equal("1.0".to_string(), "1".to_string()), true);
        assert_eq!(Solution::is_rational_equal("1.0".to_string(), "1.".to_string()), true);
        assert_eq!(Solution::is_rational_equal("0.9(9)".to_string(), "1.".to_string()), true);
        assert_eq!(Solution::is_rational_equal("0.(52)".to_string(), "0.(52)".to_string()), true);
        assert_eq!(Solution::is_rational_equal("0.1(6)".to_string(), "0.1(666)".to_string()), true);
        assert_eq!(Solution::is_rational_equal("0.(52)".to_string(), "0.5(25)".to_string()), true);
        assert_eq!(Solution::is_rational_equal("0.1666(6)".to_string(), "0.166(66)".to_string()), true);
    }
}

