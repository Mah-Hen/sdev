/* 
Mahlaki Henry
1/26/2022
Homework 2
This is my own original work 
*/
import java.util.Scanner;
public class B1 {
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        String str = getInput(in);
        System.out.printf("You entered: %s\n", str);
        System.out.printf("New Encrypted word is: %s", ceasar(str, 2));
        
    }

    public static String getInput(Scanner in){
        System.out.println("Please enter a string: ");
        String str = in.next();
        return str.toLowerCase();
    }

    public static String ceasar(String word, int offset){
        String alpha = getLowerCase();
        char [] characters = word.toCharArray();
        char [] newCharacters = new char[word.length()];
        int i;
        int charvalue;

        for (i = 0; i<characters.length; i++){
            // System.out.println((alpha.indexOf(characters[i])+offset)%26);
            charvalue = (alpha.indexOf(characters[i]) +offset)%26; // y and z is out of range of the alpha array. 
            newCharacters[i] += alpha.charAt(charvalue);

        }

        String newword = new String(newCharacters);

        
        return newword;
    }

    public static String getLowerCase(){
        String out = "";
        for (char x = 'a'; x <= 'z'; x++){
            out += Character.toString(x);
        }
        return out;
    }
}


