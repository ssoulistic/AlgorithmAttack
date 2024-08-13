class Solution {
    public int solution(int[][] sizes) {
        int length=0;
        int height=0;
        for (int[] card:sizes){
            height = Math.max(height,Math.max(card[0],card[1]));
            length = Math.max(length,Math.min(card[0],card[1]));
        }
        int answer = height*length;
        return answer;
    }
}