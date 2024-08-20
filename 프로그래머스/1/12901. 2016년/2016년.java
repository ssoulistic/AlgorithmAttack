import java.util.HashMap;
class Solution {
    public String solution(int a, int b) {
        String answer = "";
        HashMap<Integer,String> days = new HashMap<>();
        HashMap<Integer,Integer> month = new HashMap<>();
        days.put(0,"SUN");
        days.put(1,"MON");
        days.put(2,"TUE");
        days.put(3,"WED");
        days.put(4,"THU");
        days.put(5,"FRI");
        days.put(6,"SAT");
        month.put(1,31);
        month.put(2,29);
        month.put(3,31);
        month.put(4,30);
        month.put(5,31);
        month.put(6,30);
        month.put(7,31);
        month.put(8,31);
        month.put(9,30);
        month.put(10,31);
        month.put(11,30);
        month.put(12,31);
        int date=0;
        for (int i=1;i<a;i++){
            date+=month.get(i);
        }
        date+=b;
        answer=days.get((date+4)%7);
        return answer;
    }
}