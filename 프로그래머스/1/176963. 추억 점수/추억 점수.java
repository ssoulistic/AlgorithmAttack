import java.util.*;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        HashMap<String,Integer> memory = new HashMap<String,Integer>();
        for (int i=0;i<name.length;i++){
            memory.put(name[i],yearning[i]);
        }
        int[] answer = new int[photo.length];
        for (int j=0;j<photo.length;j++){
            int temp=0;
            for (int k =0;k<photo[j].length;k++){
                if (memory.get(photo[j][k])!=null){
                    temp+=memory.get(photo[j][k]);
                }
            }
            answer[j]=temp;
        }
        
        return answer;
    }
}