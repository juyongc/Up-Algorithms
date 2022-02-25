import java.io.*;
class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int number_length = phone_number.length();
        char[] number = phone_number.toCharArray();
        for (int i=0;i<number_length - 4;i++) {
            number[i] = '*';
        }
        answer = String.valueOf(number);
        return answer;
    }
}