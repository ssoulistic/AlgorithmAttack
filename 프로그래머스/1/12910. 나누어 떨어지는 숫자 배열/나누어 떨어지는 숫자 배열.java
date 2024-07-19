import java.util.ArrayList;
import java.util.Collections;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> candidates= new ArrayList<>();
        for (int i=0;i<arr.length;i++)
        {
            if(arr[i]%divisor==0)
            {
                candidates.add(arr[i]);
            }
        }
        Collections.sort(candidates);
        if (candidates.isEmpty()){
            candidates.add(-1);
            };
        int[] answer= new int[candidates.size()];
        for (int i =0;i<answer.length;i++)
        {
            answer[i]=candidates.get(i);
        }
        
        return answer;
    }
}