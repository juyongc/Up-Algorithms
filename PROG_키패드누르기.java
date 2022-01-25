import java.io.*;
import static java.lang.Math.abs;

class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int right = 12;
        int left = 10;

        for (int num : numbers) {
            if (num == 1 || num == 4 || num == 7) {
                answer += "L";
                left = num;
            } else if (num == 3 || num == 6 || num == 9) {
                answer += "R";
                right = num;
            } else {
                if (num == 0) {
                    num = 11;
                }
                int cntR = moveCnt(right,num);
                int cntL = moveCnt(left,num);
                if (cntR < cntL) {
                   answer += "R";
                   right = num;
                } else if (cntR > cntL) {
                   answer += "L";
                   left = num;
                } else {
                   if (hand.equals("right")) {
                       answer += "R";
                       right = num;
                   } else {
                       answer += "L";
                       left = num;
                   }
                }
            }
            
        }
        
        return answer;
    }
    
    int moveCnt(int current, int destiny) {
        
        int diff = abs(current - destiny);
        int share = diff / 3;
        int rem = diff % 3;
        return (share+rem);
    }
}