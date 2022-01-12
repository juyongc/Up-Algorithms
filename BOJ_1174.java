import java.io.*;
import java.util.ArrayList;
import java.util.Collections;


class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int answer = 0;
        int N = Integer.parseInt(br.readLine());

        ArrayList<Long> numList = new ArrayList<>();

        for (int k=0;k<10;k++) {
            getNumber(k, 1, numList);
        }

        Collections.sort(numList);      // 순서대로 출력할 수 있게 정렬
        // 최대 1023개 => 그 이상은 -1 출력
        if (N >= 1024) {
            System.out.println(-1);
        } else {
            System.out.println(numList.get(N-1));
        }

    }

    // 1의 자리 수보다 작은 값이 있으면 추가하기
    // 최대 10자리 (ex.9876543210)
    public static ArrayList getNumber(long num, int depth, ArrayList numList) {

        if (depth > 10) {
            return numList;
        }

        numList.add(num);

        for (int i=0;i<10;i++) {
            if ((num%10)>i) {
                getNumber((num * 10) + i, depth + 1, numList);
            }
        }

        return numList;
    }
}

