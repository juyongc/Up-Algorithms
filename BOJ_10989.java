// 카운팅 정렬
class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[] cnt = new int[10001];     // 1~10000까지의 수
        int N = Integer.parseInt(br.readLine());
        
        // 해당하는 인덱스 ++
        for (int i=0; i<N; i++) {
            cnt[Integer.parseInt(br.readLine())]++;
        }

        br.close();
        
        // 10000까지 가면서 0보다 크면 0까지 줄이면서 sb에 해당 값 append
        for(int i=0; i<10001; i++) {

            while (cnt[i] > 0) {
                sb.append(i);
                sb.append("\n");
                cnt[i]--;
            }

        }

        System.out.println(sb);

    }

}