import java.io.*;
import java.util.*;

class Main {

    public static void main(String[] args) throws IOException {

//        File file = new File("./test.txt");
//        FileReader filereader = new FileReader(file);
//        BufferedReader br = new BufferedReader(filereader);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] brInput = br.readLine().split(" ");
        int N = Integer.parseInt(brInput[0]);
        HashMap<Integer, Stack> totalLine = new HashMap<Integer, Stack>();
        // 기타 6줄 - 줄마다 스택만들기
        for (int i=1;i<7;i++) {
            totalLine.put(i, new Stack());
        }
        Stack stack;
        int cnt = 0;
        for (int i=0;i<N;i++) {
            String[] guitar = br.readLine().split(" ");
            int guitarLine = Integer.parseInt(guitar[0]);
            int fret = Integer.parseInt(guitar[1]);
            stack = totalLine.get(guitarLine);      // 해당 스택 부르기
            // 스택 empty 아니면,
            while (!stack.empty()) {
                int num = Integer.parseInt(stack.peek().toString());
                cnt += 1;
                if (fret > num) {                   // 기존 프렛보다 크면 => 추가 / break
                    stack.push(fret);
                    break;
                } else if (fret < num) {            // 기존 프렛보다 작으면 => pop
                    stack.pop();
                } else {                            // 같으면 => 넘기기
                    cnt -= 1;
                    break;
                }
            }
            if (stack.empty()) {                    // 스택 empty => 현재 프렛 추가
                stack.push(fret);
                cnt += 1;
            }
        }

        System.out.println(cnt);

    }
}

