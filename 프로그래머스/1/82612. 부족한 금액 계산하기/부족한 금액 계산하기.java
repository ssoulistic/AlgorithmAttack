class Solution {
    public long solution(int price, int money, int count) {
        long answer = (long)price* (long) (count+1)* (long) count/2-money;
        if (answer<0){answer=0;}
        return answer;
    }
}