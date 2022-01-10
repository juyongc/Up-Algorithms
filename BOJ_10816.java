import java.io.*;
import java.util.HashMap;
import java.util.StringTokenizer;


class Main {


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        HashMap<Long, Long> cardNum = new HashMap<>();

        // hashmap에 숫자 카드 넣고, 해당 값 카운팅
        for (int i=0;i<N;i++) {
            long num = Long.parseLong(st.nextToken());
            if (cardNum.containsKey(num)) {
                cardNum.put(num, cardNum.get(num) + 1);
            } else {
                cardNum.put(num, (long) 1);
            }
        }

        int M = Integer.parseInt(br.readLine());
        StringTokenizer stM = new StringTokenizer(br.readLine(), " ");

        String[] ans = new String[M];
        
        // ans 리스트에 해당 값 추가
        for (int i=0;i<M;i++) {
            long numM = Long.parseLong(stM.nextToken());
            if (cardNum.containsKey(numM)) {
                ans[i] = cardNum.get(numM).toString();
            } else {
                ans[i] = "0";
            }
        }

        for (int i=0;i<M;i++) {
            bw.write(ans[i] + " ");
        }

        bw.close();
        br.close();

    }
}

