import java.util.Stack;

public class Solution {
    public boolean checkValidString(String s) {
        Stack<Integer> s1 = new Stack<>();
        Stack<Integer> s2 = new Stack<>();
        char[] ch = s.toCharArray();
        for(int i =0;i<ch.length;i++){
            if(ch[i]=='(') s1.push(i);
            else if(ch[i]=='*') s2.push(i);
            else{
                if(!s1.isEmpty()) s1.pop();
                else if(!s2.isEmpty()) s2.pop();
                else return false;
            }
        }
        while (!s1.isEmpty()&&!s2.isEmpty()){
            int indexS1 = s1.pop();
            int indexS2 = s2.pop();
            if(indexS1>indexS2) return false;
        }
        return s1.isEmpty();
    }
}
