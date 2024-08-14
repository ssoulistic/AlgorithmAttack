import java.util.HashMap;
import java.util.Arrays;
import java.io.*;
class Solution {
    public int solution(String s) {
        StringBuilder answer = new StringBuilder();
        HashMap<String,String> map = new HashMap<>(){{
            put("one","1");
            put("two","2");
            put("three","3");
            put("four","4");
            put("five","5");
            put("six","6");
            put("seven","7");
            put("eight","8");
            put("nine","9");
            put("zero","0");
        }};
        char[] chars=s.toCharArray();
        StringBuilder st = new StringBuilder();
        for (char s1:chars){
            if (Character.isDigit(s1)){
                answer.append(s1);
            }
            else{
                st.append(s1); 
                if (map.get(st.toString())!=null){
                    answer.append(map.get(st.toString()));
                    st.setLength(0);
                }
            }
        }
        if (map.get(st.toString())!=null){
                    answer.append(map.get(st.toString()));
                    st.setLength(0);
            }
        
        
        return Integer.valueOf(answer.toString());
    }
}