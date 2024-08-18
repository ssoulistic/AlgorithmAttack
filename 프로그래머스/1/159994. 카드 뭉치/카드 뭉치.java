class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "No";
        int i=0,j=0,k=0;
        while (i<cards1.length & j<cards2.length & k<goal.length){
            if (goal[k].equals(cards1[i])){
                i++;
                k++;
            }
            else if(goal[k].equals(cards2[j])){
                j++;
                k++;
            }
            else{
                break;
            }
        }
        if (i==cards1.length){
            while (j<cards2.length & k<goal.length){
                if(goal[k].equals(cards2[j])){
                    j++;
                    k++;
            }
                else{
                    break;
                }
            }
        }
        else if (j==cards2.length){
            while (i<cards1.length &  k<goal.length){
                if (goal[k].equals(cards1[i])){
                i++;
                k++;
            }
                else{
                    break;
                }
            }
        }
        
        if (k==goal.length){
            answer="Yes";
        }
        return answer;
    }
}