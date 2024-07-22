import java.util.ArrayList;
class Solution {
    public int[] solution(int[] arr) {
        int smallest = Integer.MAX_VALUE;
        int smallest_idx = 0;
        
        ArrayList<Integer> result = new ArrayList<>();
        for (int i=0; i<arr.length;i++)
        {
            if (arr[i]<smallest)
            {
                smallest=arr[i];
                smallest_idx=i;
            }
        }
        for (int j =0;j<arr.length;j++)
        {
            if (j!=smallest_idx)
            {
                result.add(arr[j]);
            }
        }
        int[] answer;
        answer= new int[]{-1};
        if (result.size()!=0){
            answer = new int[result.size()];
            for (int j=0;j<result.size();j++)
            {
                answer[j] = result.get(j);
            }
        }
        return answer;
    }
}