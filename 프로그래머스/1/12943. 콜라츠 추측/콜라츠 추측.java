class Solution {
    public int solution(int num) {
        int count =0;
        if (num==1){
            return 0;
        }
        long answer=(long)num;
        while(count<500 && answer!=1){
            if (answer%2==0){
                answer/=2;
            }
            else{
                answer*=3;
                answer+=1;
            }
            count+=1;
        }
        if (count<500) return count;
        else return -1;
    }
}