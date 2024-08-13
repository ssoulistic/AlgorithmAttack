import java.util.HashMap;
class Solution {
    public int[] solution(String s) {
        String[] word=s.split("");
        int[] answer = new int[s.length()];
        HashMap<String,Integer> map = new HashMap<>();
        for (int i=0;i<s.length();i++){
            if (map.get(word[i])!=null) {
                answer[i]=i-map.get(word[i]);
                map.put(word[i],i);
            }
            else{
                answer[i]=-1;
                map.remove(word[i]);
                map.put(word[i],i);
            }
        }
        
        
        
        
        return answer;
    }
}