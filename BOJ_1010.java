import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// dp - 파스칼 법칙
class Main {

    static int[][] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int i=0; i<T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            dp = new int[M+1][N+1];
            int ans = combi(M, N);
            sb.append(ans).append("\n");
        }

        System.out.println(sb);
        br.close();

    }

    static int combi(int n, int r) {

        // 이미 계산한 값이면 해당 값 반환
        if (dp[n][r] > 0) {
            return dp[n][r];
        }
        // 처음,마지막 = 1 반환
        if (n==r || r == 0) {
            return dp[n][r] = 1;
        }
        // 파스칼 법칙
        return dp[n][r] = combi(n - 1, r - 1) + combi(n - 1, r);
    }

}

