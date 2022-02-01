import java.io.*;
import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        
        int[] answer = new int[n+1];
        Arrays.sort(lost);
        Arrays.sort(reserve);
        for (int i=0;i<n+1;i++){
            answer[i] = 1;
        }
        for (int los : lost) {
            answer[los] -= 1;
        }

        int[] visit = new int[reserve.length];
        for (int i =0; i < reserve.length; i++) {
            if (answer[reserve[i]]==0) {
                visit[i] = 1;
                answer[reserve[i]] = 1;
            }
        }

        for (int i =0; i < reserve.length; i++) {
            if (visit[i] == 0) {
                int resMinus = reserve[i] - 1;
                int resPlus = reserve[i] + 1;
                if (resMinus > 0 && answer[resMinus] == 0) {
                    answer[resMinus] += 1;
                } else if (resPlus < n+1 && answer[resPlus] == 0) {
                    answer[resPlus] += 1;
                }
            }
        }

        int cnt = 0;
        for (int i =1; i < n+1; i++) {
            if (answer[i] > 0) {
                cnt += 1;
            }
        }
        
        return cnt;
    }
}