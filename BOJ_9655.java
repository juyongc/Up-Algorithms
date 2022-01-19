import java.io.*;


class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String answer = whoLast(N);

        System.out.println(answer);
        br.close();
    }

    static String whoLast(int N) {
        int idx = 0;
        int cnt = 0;
        while (idx < N) {
            if (idx + 3 <= N) {
                idx += 3;
            } else {
                idx += 1;
            }
            cnt += 1;
        }

        if (cnt % 2 == 1) {
            return "SK";
        } else {
            return "CY";
        }
    }

}
