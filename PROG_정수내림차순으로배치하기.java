import java.io.*;
import java.util.*;
class Solution {
    public long solution(long n) {
        String num = String.valueOf(n);
        char[] arr = num.toCharArray();
        Arrays.sort(arr);
        String conv = new StringBuilder(new String(arr)).reverse().toString();
        long answer = Long.parseLong(conv);

        return answer;
    }
}