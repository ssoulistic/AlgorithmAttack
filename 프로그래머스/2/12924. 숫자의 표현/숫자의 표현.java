class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i=1;i<=n;i++){
            int acc=0;
            for (int j =i; j<=n;j++)
            {
                acc+=j;
                if (acc==n){
                    answer+=1;
                }
                else if (acc>n){
                    break;
                }
            }
        }
        return answer;
    }
}