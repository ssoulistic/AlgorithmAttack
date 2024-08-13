class Solution {
    public int solution(int[][] sizes) {
        int min_size=0;
        int max_size=0;
        
        int answer = 0;
        for (int i=0; i<sizes.length; i++){
            if (max_size<Math.max(sizes[i][0],sizes[i][1])){
                max_size=Math.max(sizes[i][0],sizes[i][1]);
            }
            if (min_size<Math.min(sizes[i][0],sizes[i][1])){
                min_size=Math.min(sizes[i][0],sizes[i][1]);
            }
            
        }
        answer=min_size*max_size;
        return answer;
    }
}