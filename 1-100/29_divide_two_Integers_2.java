class Solution {
    public int divide(int dividend, int divisor) {
        boolean dividendNeg = dividend < 0;
        boolean divisorNeg = divisor < 0;

        if (!divisorNeg) {
            divisor = -divisor;
        }
        if (!dividendNeg) {
            dividend = -dividend;
        }

        List<Integer> tmp = new ArrayList<>();
        tmp.add(divisor);
        while ((dividend < divisor)) {
            divisor = divisor << 1;
            if (divisor > 0){
                break;
            }
            tmp.add(divisor);
        }

        int answer = 0;
        while (!tmp.isEmpty()) {
            Integer last = tmp.get(tmp.size() - 1);
            if (dividend <= last) {
                dividend -= last;
                answer += multiplyN(tmp.size());
            }
            tmp.remove(tmp.size() - 1);
        }

        if ((dividendNeg && !divisorNeg) || (!dividendNeg && divisorNeg)) {
            return -answer;
        }

        if (answer == Integer.MIN_VALUE) {
            answer = Integer.MAX_VALUE;
        }

        return answer;
    }

    public int multiplyN(int n) {
        int ret = 1;
        for (int i = 1; i < n; i += 1) {
            ret *= 2;
        }
        return ret;
    }
}