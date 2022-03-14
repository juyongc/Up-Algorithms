import java.io.*;
import java.util.*;

class Main {

    public static void main(String[] args) throws IOException {

//        File file = new File("./test.txt");
//        FileReader filereader = new FileReader(file);
//        BufferedReader br = new BufferedReader(filereader);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split(" ");
        ArrayList intArr = new ArrayList<Long>();
        for (String s : arr) {
            long val = Long.parseLong(s);
            intArr.add(val);
        }
        int s = 0;
        int e = intArr.size()-1;
        long[] answer = {2000000001,0,0};
        while (s < e) {
            long minus = ((Long) intArr.get(e)) + ((Long) intArr.get(s));
            long absolute = Math.abs(minus);
            if (absolute < answer[0]) {
                answer[0] = absolute;
                answer[1] = (Long) intArr.get(s);
                answer[2] = (Long) intArr.get(e);
            }
            if (minus > 0) {
                e -= 1;
            } else if (minus < 0) {
                s += 1;
            } else {
                break;
            }
        }
        System.out.println(String.valueOf(answer[1]) + " " + String.valueOf(answer[2]));
    }
}
