import java.util.Stack;
class Solution {
    boolean solution(String s) {
        Stack<Character> list = new Stack<>();
        for (char c:s.toCharArray()){
            if (c=='('){
                list.push('(');
            }
            else{
                if (list.isEmpty()){
                    return false;
                 }
                list.pop();
            }
        }
        
        return list.isEmpty();
    }
}