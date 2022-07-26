import java.io.*;
import java.util.*;

class Main {

    public static void main(String[] args) throws IOException {
//        File file = new File("./test.txt");
//        FileReader filereader = new FileReader(file);
//        BufferedReader br = new BufferedReader(filereader);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int answer = 0;
        
        ArrayDeque<Integer> deq = new ArrayDeque<>();       // Deque 사용 - FIFO 사용하기 위해
        HashMap<Integer, Integer> map = new HashMap<>();    // map - 중복 감지 위해 사용
        deq.add(N);
        map.put(N, 0);
        int now,cnt;
        // deq에 값이 있다면 반복
        // 조건에 맞게, 3으로 나눈 값, 2로 나눈 값, 1 뺀값에서 1이 나올 때까지 찾기
        while (!deq.isEmpty()) {
            now = deq.poll();
            cnt = map.get(now);
            if (now == 1) {
                answer = cnt;
                break;
            }
            if (now % 3 == 0) {
                int three = now / 3;
                if (three == 1) {
                    answer = cnt + 1;
                    break;
                }
                if (!map.containsKey(three)) {
                    map.put(three, cnt + 1);
                    deq.add(three);
                }
            }
            if (now % 2 == 0) {
                int two = now / 2;
                if (two == 1) {
                    answer = cnt + 1;
                    break;
                }
                if (!map.containsKey(two)) {
                    map.put(two, cnt + 1);
                    deq.add(two);
                }
            }
            int minus = now - 1;
            if (minus == 1) {
                answer = cnt + 1;
                break;
            }
            if (!map.containsKey(minus)) {
                map.put(minus, cnt + 1);
                deq.add(minus);
            }
        }
        System.out.println(answer);
    }
}

