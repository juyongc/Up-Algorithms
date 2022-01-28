import java.io.*;
import java.util.HashMap;
class Solution {
    public String solution(String[] participants, String[] completions) {
        String answer = "";
        
        HashMap<String, Integer> names = new HashMap();
        for (String participant: participants) {
            if (names.get(participant) != null) {
                names.put(participant, names.get(participant)+1);
            } else {
                names.put(participant, 1);
            }
        }

        for (String comp: completions) {
            if (names.get(comp) != null) {
                if (names.get(comp) > 1) {
                    names.put(comp, names.get(comp) - 1);
                } else {
                    names.remove(comp);
                }
            }
        }
        for (String ans: names.keySet()) {
            answer = ans;
            break;
        }
        
        return answer;
        
    }
}