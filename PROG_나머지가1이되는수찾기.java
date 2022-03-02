class Solution {
    public int solution(int n) {
        int share = n - 1;
        int answer = 0;
        for (int i=2;i<=share;i++) {
            int rem = share % i;
            if (rem == 0) {
                answer = i;
                break;
            }
        }
        return answer;
    }
}