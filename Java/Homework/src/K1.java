/* 
Mahlaki Henry
3/11/2022
Homework 11
This is my own original work 
*/

import java.util.ArrayList;
import java.util.List;

public class K1 {

    public static int [] matchElements(seq S1, seq S2){
        int [] list1 = S1.getSeq();
        List<Integer> matchingElements = new ArrayList<>();
        

        for(int i = 0; i<S2.getSeq().length; i++){
            int x = S2.getSeq()[i];
            for(int j = 0; j<list1.length;j++){
                if (x == list1[j]) {
                    matchingElements.add(x);
                    break;}
            }
        }

        int [] result = new int [matchingElements.size()];
        for (int i = 0; i<matchingElements.size();i++){
                result[i] = matchingElements.get(i);
        }

        return result;
    }

    public static boolean inCommon(seq seq1 ,seq seq2){
        int [] list1 = seq1.getSeq();
        boolean match = false;
        

        for(int i = 0; i<seq2.getSeq().length; i++){
            int x = seq2.getSeq()[i];
            for(int j = 0; j<list1.length;j++){
                if (x == list1[j]) {
                    match =  true;
                    break;}
            }
        }

        return match;
        
    } 

    public static void main(String args[]){
        seq test1 = new seq(1,3,12);
        System.out.println(test1.toString());
        seq test2 = new seq(5, 5, 10);
        System.out.println(test2);

        boolean found = inCommon(test1, test2);
        int [] val = matchElements(test1, test2);

        if (found){
            System.out.printf("First in common is %d", val[0]);
        }
        else{
            System.out.println("no match");
            }
    }
    
    
}
