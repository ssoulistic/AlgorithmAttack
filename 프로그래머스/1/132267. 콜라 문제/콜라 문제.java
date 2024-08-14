class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        int quotient =0;
        int remainder =0;
        while (n>=a){
            quotient=n/a*b;
            remainder = n%a;
            n=quotient+remainder;
            answer+=quotient;
        }
        return answer;
    }
}