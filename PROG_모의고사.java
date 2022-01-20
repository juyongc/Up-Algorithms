import java.util.Arrays;

class Solution {
    public int[] solution(int[] answers) {
        
        int[] p1 = {1, 2, 3, 4, 5};
        int[] p2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] p3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int[][] correct = new int[3][2];
        for(int i=0;i<3;i++) {
            correct[i][0] = 0;
            correct[i][1] = i+1;
        }
        
        for (int i=0;i < answers.length;i++) {
            int ansP1 = i % p1.length;
            if (p1[ansP1] == answers[i]) {
                correct[0][0] += 1;
            }
            int ansP2 = i % p2.length;
            if (p2[ansP2] == answers[i]) {
                correct[1][0] += 1;
            }
            int ansP3 = i % p3.length;
            if (p3[ansP3] == answers[i]) {
                correct[2][0] += 1;
            }
        }
        
        Arrays.sort(correct, (o1, o2) -> {
            if (o1[0] == o2[0]) {
                return o1[1] - o2[1];
            } else {
                return o2[0] - o1[0];
            }
        });
        
        int maxi = correct[0][0];
        int cnt = 0;
        for (int i=0; i<3; i++) {
            if (correct[i][0] == maxi) {
                cnt += 1;
            } else {
                break;
            }
        }
        int[] answer = new int[cnt];
        for (int i=0; i<cnt; i++) {
             answer[i] = correct[i][1];
        }
        return answer;
    }
}