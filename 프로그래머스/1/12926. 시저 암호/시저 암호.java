import java.util.Arrays;
class Solution {
    public String solution(String s, int n) {
        char[] ss=s.toCharArray();
        String answer = "";
        for (char c:ss){
            if (c==' '){
                answer+=" ";
            }
            else{
                if (c-'a'>=0){
                    answer+=(char)('a' + (c-'a'+n) % 26);
                }
                else{
                    answer+=(char)('A' + (c-'A'+n) % 26);
                }
            }
        }
        
        return answer;
    }
}