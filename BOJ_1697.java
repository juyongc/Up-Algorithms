import java.io.*;
import java.util.*;


class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] dp = new int[100001];
        for (int i=0; i < dp.length; i++) {
            dp[i] = -1;
        }
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        dp[N] = 0;
        // 현재 위치가 같지 않다면
        if (N != K) {
            Queue<Integer> q = new LinkedList<>();
            q.add(N);
            // 큐에 값이 없을 때까지 반복
            while(!q.isEmpty()) {
                int now = q.poll();
                int cnt = dp[now] + 1;
                // K보다 값이 크면 => 뒤로만 움직이기
                // 같으면 => 필요없음
                // 작으면 => +1,-1,x2 다 하기
                if(now > K) {
                    int back = now - 1;
                    if (back < 0) {
                        continue;
                    }
                    if (dp[back] == -1 || dp[back] > cnt) {
                        dp[back] = cnt;
                        q.add(back);
                    }
                } else if (now == K) {
                    continue;
                } else {
                    int[] variousMove = new int[3];
                    variousMove[0] = now - 1;
                    variousMove[1] = now + 1;
                    variousMove[2] = 2 * now;
                    for (int i = 0; i < 3; i++) {
                        if (variousMove[i] < 0 || variousMove[i] > dp.length) {
                            continue;
                        }
                        if (dp[variousMove[i]] == -1 || dp[variousMove[i]] > cnt) {
                            dp[variousMove[i]] = cnt;
                            q.add(variousMove[i]);
                        }
                    }
                }
            }
        }
        br.close();
        System.out.println(dp[K]);
    }

}

