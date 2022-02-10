import java.io.*;
import java.util.*;

class Main {

    public static void main(String[] args) throws IOException {
        int[] arr = {4, 3, 2, 1};

        if (arr.length == 1) {
            int[] answer = {-1};
        }
        int mini = arr[0];
        int idx = 0;
        for (int i=1;i<arr.length;i++) {
            if (arr[i] < mini) {
                idx = i;
                mini = arr[i];
            }
        }
        List<Integer> list = new ArrayList<Integer>();
        for (int i=0;i<arr.length;i++) {
            if (i == idx) {
                continue;
            }
            list.add(arr[i]);
        }

        int[] answer = new int[list.size()];
        for (int i=0;i<list.size();i++) {
            answer[i] = list.get(i);
        }
        System.out.println(Arrays.toString(answer));
    }
}

