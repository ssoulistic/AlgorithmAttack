class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for (int i=0;i<n;i++){
            String s1=Integer.toBinaryString(arr1[i]);
            String s2=Integer.toBinaryString(arr2[i]);
            String temp="";
            for (int j=0;j<n-s1.length();j++){
                temp+="0";
            }
            String temp2="";
            for (int k=0;k<n-s2.length();k++){
                temp2+="0";
            }
            s1=temp+s1;
            s2=temp2+s2;
            StringBuilder st = new StringBuilder();
            for (int l=0;l<n;l++){
                if (s1.charAt(l)=='1' | s2.charAt(l)=='1'){
                    st.append("#");
                }
                else{
                    st.append(" ");
                }
            }
            answer[i]=st.toString();
        }
        
        return answer;
    }
}