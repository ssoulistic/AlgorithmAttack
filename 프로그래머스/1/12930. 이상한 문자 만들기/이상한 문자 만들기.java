import java.util.Arrays;
class Solution {
    public String solution(String s) {
        StringBuilder answer= new StringBuilder();
        int even = 0;
        String[] c=s.split("");
        for (int i=0;i<c.length;i++){
            if (c[i].equals(" ")){
                answer.append(" ");
                even=0;
            }
            else{
                if (even % 2==0){
                    answer.append(c[i].toUpperCase());
                }
                else{
                    answer.append(c[i].toLowerCase());
                }
                even++;
            }
        }
        return answer.toString();
    }
}