import java.util.HashSet;
import java.util.Arrays;
class Solution {
    public int[] solution(int[] numbers) {
        HashSet<Integer> result = new HashSet<>();
        for (int i=0;i<numbers.length;i++){
            for(int j=i+1;j<numbers.length;j++){
                result.add(numbers[i]+numbers[j]);
            }
        }
        int[] answer=result.stream().mapToInt(Integer::intValue).toArray();
        Arrays.sort(answer);
        return answer;
    }
}