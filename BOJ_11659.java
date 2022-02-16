import java.io.*;
import java.util.*;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        String[] arr = br.readLine().split(" ");
        int[] arrInt = new int[N];
        arrInt[0] = Integer.parseInt(arr[0]);
        for (int i=1;i < N;i++) {
            arrInt[i] = arrInt[i-1] + Integer.parseInt(arr[i]);
        }
        for (int i=0;i < M;i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st2.nextToken());
            int e = Integer.parseInt(st2.nextToken());
            if (s == 1) {
                System.out.println(arrInt[e-1]);
            } else {
                System.out.println(arrInt[e-1] - arrInt[s-2]);
            }
        }
        br.close();
    }
}
