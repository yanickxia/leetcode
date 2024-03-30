pub struct Solution;

impl Solution {
    pub fn print_vertically(s: String) -> Vec<String> {
        let strs = s.split_whitespace().collect::<Vec<&str>>();
        println!("{:?}", strs);


        let max = strs.iter()
            .map(|x| x.len())
            .max()
            .unwrap();

        let mut result = Vec::<String>::new();
        for i in 0..max {
            result.push("".to_string())
        }

        let mut current_index = 0 as usize;

        for i in 0..max {
            for j in 0..strs.len() {
                if strs[j].len() > current_index {
                    result[i] = result[i].to_string() + &(strs[j][current_index..current_index + 1])
                }else{
                    result[i] = result[i].to_string() + " "
                }
            }
            current_index += 1
        }

        let result = result.iter()
            .map(|it| it.trim_end_matches(" "))
            .filter(|p| p.len() > 0)
            .map(|x| x.to_string())
            .collect::<Vec<String>>();

        return result;
    }
}

#[cfg(test)]
mod tests {
    use crate::*;

    #[test]
    fn it_works() {
        assert_eq!(Solution::print_vertically("HOW ARE YOU".to_string()), vec!["HAY", "ORO", "WEU"]);
        assert_eq!(Solution::print_vertically("TO BE OR NOT TO BE".to_string()), vec!["TBONTB", "OEROOE", "   T"]);
        assert_eq!(Solution::print_vertically("CONTEST IS COMING".to_string()), vec!["CIC", "OSO", "N M", "T I", "E N", "S G", "T"]);
    }
}

