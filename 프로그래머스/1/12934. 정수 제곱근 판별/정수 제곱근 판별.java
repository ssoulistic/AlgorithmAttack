class Solution {
    public long solution(long n) {
        for(int i=1; i<=n;i++){
            if (n%i==0 & n/i==i){
                return (long)(i+1)*(i+1);
            }
        }        
        return -1;
    }
}