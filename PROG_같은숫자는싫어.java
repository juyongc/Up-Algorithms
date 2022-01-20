import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<Integer>();
        
        int now = arr[0];
        list.add(now);
        
        for (int num: arr) {
            if (num != now) {
                now = num;
                list.add(now);
            }
        }
        int[] answer = new int[list.size()];
        for (int i=0;i<list.size();i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}
