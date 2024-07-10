class Solution {
    public boolean solution(int x) {
        int acc=0;
        int y =x;
        while (x>0){
            acc+=x%10;
            x=x/10;
        }
        if (y%acc==0){
            return true;    
        }
        return false;
    }
}