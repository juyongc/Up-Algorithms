class Solution {
    public String solution(int a, int b) {
        String answer = "";
        int[] month = {0,31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int day = -1;
        for (int i =1; i<a;i++) {
            day += month[i];
        }
        day += b;
        day = day % 7;
        String[] days = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
        answer = days[day];
        return answer;
    }
}