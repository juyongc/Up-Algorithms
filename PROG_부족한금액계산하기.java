class Solution {
    public long solution(int price, int money, int count) {
        
        long tot = 0;
        for (int i=1; i < count+1; i++) {
            tot += i;
        }

        long answer = 0;
        answer = money - (tot * price);
        if (answer >= 0) {
            answer = 0;
        } else {
            answer = -answer;
        }
        return answer;
    }
}