class Solution {
    public double solution(int[] arr) {
        double tot = 0;
        for (int i : arr) {
            tot += i;
        }
        double answer = tot / arr.length;
        return answer;
    }
}