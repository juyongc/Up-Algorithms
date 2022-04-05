import java.io.*;
import java.util.*;

class Main {

    public static void main(String[] args) throws IOException {

//        File file = new File("./test.txt");
//        FileReader filereader = new FileReader(file);
//        BufferedReader br = new BufferedReader(filereader);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String N = "9" + br.readLine();
        if (N.length() < 2) {
            System.out.println(0);
            return;
        }
        int[] dp = new int[N.length()];
        dp[0] = 1;
        int flag; int current; int value;
        for (int i=1;i<N.length();i++) {
            flag = 0;
            current = Integer.parseInt(String.valueOf(N.charAt(i)));
            // 현재값 => 1~9만 허용
            if (0 < current && current < 10) {
                dp[i] += dp[i - 1];
                flag = 1;
            }
            value = Integer.parseInt(String.valueOf(N.charAt(i - 1)) + String.valueOf(N.charAt(i)));
            // 이전값과 자릿수 더한 값 => 10~26만 허용
            if (9 < value && value < 27) {
                dp[i] += dp[i - 2];
                flag = 1;
            }
            if (flag == 0) {
                System.out.println(0);
                return;
            }
            dp[i] %= 1000000;
        }
        System.out.println(dp[N.length()-1]);
    }
}

