class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        int[] divs=new int[number];
        for (int i=0;i<number;i++){
            for (int j=i+1;j<=number;j+=i+1){
                divs[j-1]++;
            }
        }
        for (int k=0;k<divs.length;k++){
            if (divs[k]>limit){
                answer+=power;
            }
            else{
                answer+=divs[k];
            }
        }
        
        return answer;
    }
}