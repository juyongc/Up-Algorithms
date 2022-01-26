import java.util.Arrays;
class Solution {
    
    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        for (int num : d) {
            budget -= num;
            if (budget < 0) {
                break;
            } else {
                answer += 1;
            }
        }
        return answer;
    }
}