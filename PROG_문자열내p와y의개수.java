import java.io.*;
import java.util.*;
class Solution {
    boolean solution(String word) {
        boolean answer = true;
        int p = 0;
        int y = 0;
        Set<Character> setP = new HashSet<>(Arrays.asList('p','P'));
        Set<Character> setY = new HashSet<>(Arrays.asList('y','Y'));
        for (int i=0;i<word.length();i++) {
            if (setP.contains(word.charAt(i))) {
                p += 1;
            } else if (setY.contains(word.charAt(i))) {
                y += 1;
            }
        }
        if (p != y) {
            answer = false;
        }
        return answer;
    }
}