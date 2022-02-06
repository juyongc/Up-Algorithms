import java.io.*;
import java.util.*;

class Solution {
    
    public int[] slice(int[] array, int s, int e) {
        int[] arr = new int[e - s + 1];
        for (int i=s;i < e+1; i++) {
            arr[i-s] = array[i];
        }
        return arr;
    }
    
    public int[] solution(int[] array, int[][] commands) {
        int tot = commands.length;
        int[] answer = new int[tot];
        for (int i=0;i<tot;i++) {
            int[] sliceArr = slice(array, commands[i][0]-1, commands[i][1]-1);
            Arrays.sort(sliceArr);
            answer[i] = sliceArr[commands[i][2]-1];
        }
        return answer;
    }
}