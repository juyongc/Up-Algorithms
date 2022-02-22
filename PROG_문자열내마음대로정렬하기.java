import java.io.*;
import java.util.*;
class Solution {
    public String[] solution(String[] words, int n) {
        int wordLength = words.length;
        String[] answer = new String[wordLength];
        String[] cwords = new String[wordLength];
        int cnt = 0;
        for (String word : words) {
            String nword = word.charAt(n) + word;
            cwords[cnt] = nword;
            cnt++;
        }
        Arrays.sort(cwords);
        cnt = 0;
        for (String cword : cwords) {
            answer[cnt] = cword.substring(1);
            cnt++;
        }
        return answer;
    }
}