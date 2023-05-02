public class stacker {
    public static void main(String args[]){
        Stack <String> s1 = new Stack <String>();
        s1.push("{");
        s1.push("}");
        System.out.println(s1.toString()); 
        s1.pop(); 
        System.out.println(s1.peek());   
    
}

    public String getInput(){
        return "";
    }

    public boolean isBalanced(String expression){
        return false;
    }
}
