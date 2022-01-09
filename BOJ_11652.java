import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

import static java.lang.Math.min;


class Main {


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        HashMap<Long, Long> cardNum = new HashMap<>();
        
        // hashmap에 숫자 카드 넣고, 해당 값 카운팅
        for (int i=0;i<N;i++) {
            long num = Long.parseLong(br.readLine());
            if (cardNum.containsKey(num)) {
                cardNum.put(num, cardNum.get(num) + 1);
            } else {
                cardNum.put(num, (long) 1);
            }
        }
        long cnt = 0;
        long ans = 0;
        // 가장 많은(cnt), 가장 작은 수(ans) 찾기
        for (Long keyVal : cardNum.keySet()) {
            if (cardNum.get(keyVal) > cnt) {
                ans = keyVal;
                cnt = cardNum.get(keyVal);
            } else if (cardNum.get(keyVal) == cnt) {
                ans = min(ans, keyVal);
            }
        }

        System.out.println(ans);
    }
}

