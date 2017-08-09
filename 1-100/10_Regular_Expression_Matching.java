package info.yannxia.kotlion;

/**
 * Created by yann on 2017/2/7.
 */
public class Solution {

    private State begin = new State();
    private static final Character SPITE = '#';
    private static final Character END = '@';

    public void parse(String pattern, State current) {

        if (pattern.isEmpty()) {
            current.c = END;
            return;
        }

        if (pattern.length() > 1 && pattern.charAt(1) == '*') {
            current.c = SPITE;
            current.out1 = new State();
            current.out1.c = pattern.charAt(0);
            current.out1.out1 = current;
            current.out2 = new State();
            parse(pattern.substring(2), current.out2);
        } else if (Character.isAlphabetic(pattern.charAt(0)) || pattern.charAt(0) == '.') {
            current.c = pattern.charAt(0);
            current.out1 = new State();
            parse(pattern.substring(1), current.out1);
        }
    }


    public boolean run(String str, State current) {
        if (str.isEmpty() && current.c == END) {
            return true;
        }

        if (current.c == SPITE) {
            return run(str, current.out1) || run(str, current.out2);
        }

        if (!str.isEmpty() && (current.c == str.charAt(0) || current.c == '.')) {
            return run(str.substring(1), current.out1);
        }

        return false;
    }


    public boolean isMatch(String s, String p) {
        Solution solution = new Solution();
        solution.parse(p, this.begin);
        return solution.run(s, this.begin);
    }


    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.parse(".*", solution.begin);
        solution.run("aa", solution.begin);
    }

}

class State {
    State out1;
    State out2;
    char c;
}
