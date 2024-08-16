import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        ArrayList<Integer> board = new ArrayList<Integer>();
        for (int i=0;i<score.length;i++){
            board.add(score[i]);
            Collections.sort(board,Collections.reverseOrder());
            if (k>board.size()){
                    answer[i]=board.get(board.size()-1);
                }
            else{
                answer[i]=board.get(k-1);
            }
        }
        return answer;
    }
}