import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        HashSet<Integer> numSet = new HashSet<Integer>();

        for (int i=0;i< numbers.length;i++){
            for (int j=i+1;j< numbers.length;j++) {
                numSet.add(numbers[i] + numbers[j]);
            }
        }

        ArrayList<Integer> numList = new ArrayList<Integer>(numSet);
        Collections.sort(numList);
        
        int[] answer = new int[numList.size()];
        for (int i=0; i < numList.size();i ++) {
            answer[i] = numList.get(i).intValue();
        }
        return answer;
    }
}