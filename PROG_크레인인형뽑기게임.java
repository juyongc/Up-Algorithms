import java.io.*;
import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int row = board.length;
        int col = board[0].length;
        int answer = 0;
        
        Stack<Integer> stack = new Stack<>();
        for (int move : moves) {
            int now = move - 1;
            for (int i = 0; i < row; i++) {
                if (board[i][now] != 0) {
                    int doll = board[i][now];
                    if (!stack.empty()) {
                        int last = stack.pop();
                        if (last == doll) {
                            answer += 2;
                        } else {
                            stack.push(last);
                            stack.push(doll);
                        }
                    } else {
                        stack.push(doll);

                    }
                    board[i][now] = 0;
                    break;
                }
            }
        }
        
        return answer;
    }
}