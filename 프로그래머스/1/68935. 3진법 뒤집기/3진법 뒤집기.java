import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        Stack<Integer> st = new Stack<>();
        while (n>0){
            st.push(n%3);
            n/=3;
        }
        int stlen=st.size();
        for (int i=0; i<stlen;i++){
            answer+=st.pop()*Math.pow(3,i);
        }
        
        
        return answer;
    }
}