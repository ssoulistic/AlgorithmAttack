import java.util.Set;
import java.util.HashSet;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashSet<Integer> set = new HashSet<>();
        for (int i=0;i<nums.length;i++){
            set.add(nums[i]);
        }
        answer=Math.min(set.size(),nums.length/2);
        return answer;
    }
}