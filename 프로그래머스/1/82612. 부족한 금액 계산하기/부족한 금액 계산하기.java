class Solution {
    public long solution(long price, long money, long count) {
        return price*count*(count+1)/2-money>0?price*count*(count+1)/2-money:0;
    }
}