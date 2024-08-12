import java.util.Arrays;
class Solution {
    public String solution(String s) {
        String answer="";
        int even = 0;
        String[] c=s.split("");
        for (int i=0;i<c.length;i++){
            if (c[i].equals(" ")){
                answer+=" ";
                even=0;
            }
            else{
                if (even % 2==0){
                    answer+=c[i].toUpperCase();
                }
                else{
                    answer+=c[i].toLowerCase();
                }
                even+=1;
            }
        }
        return answer;
    }
}