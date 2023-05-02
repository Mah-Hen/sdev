import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


/* 
Mahlaki Henry
2/8/2022
Homework 5
This is my own original 
*/
public class Main {

    public static <T> void listofThings(){
        List <ThreeNames> things = new ArrayList<ThreeNames>(10);
        ThreeNames one = new ThreeNames();
        ThreeNames two = new ThreeNames();
        ThreeNames three = new ThreeNames();
        ThreeNames four = new ThreeNames();
        ThreeNames five = new ThreeNames();
        ThreeNames six = new ThreeNames();
        ThreeNames seven = new ThreeNames();
        ThreeNames eight = new ThreeNames();
        ThreeNames nine = new ThreeNames();
        ThreeNames ten = new ThreeNames();
        one.assign(0, "John");
        one.assign(1, "Jane");
        one.assign(2, "Doe");
        things.add(one);
        two.assign(0, "Jack");
        two.assign(1, "Jill");
        two.assign(2, "Green");
        things.add(two);
        three.assign(0, "A");
        three.assign(1, "B");
        three.assign(2, "C");
        things.add(three);
        four.assign(0, "D");
        four.assign(1, "E");
        four.assign(2, "F");
        things.add(four);
        five.assign(0, "G");
        five.assign(1, "H");
        five.assign(2, "I");
        things.add(five);
        six.assign(0, "J");
        six.assign(1, "K");
        six.assign(2, "L");
        things.add(six);
        seven.assign(0, "M");
        seven.assign(1, "N");
        seven.assign(2, "O");
        things.add(seven);
        eight.assign(0, "P");
        eight.assign(1, "Q");
        eight.assign(2, "R");
        things.add(eight);
        nine.assign(0, "S");
        nine.assign(1, "T");
        nine.assign(2, "U");
        things.add(nine);
        ten.assign(0, "V");
        ten.assign(1, "W");
        ten.assign(2, "X");
        things.add(ten);

        System.out.println("Before Sorting:");
        for (Object thing: things){
            System.out.println(thing);
        }

        Collections.sort(things);
        
        System.out.println("\nAfter Sorting");
        for (Object thing: things){
            System.out.println(thing);
        }
    }

    public static void main(String[] args) throws Exception {
        ThreeNames one = new ThreeNames();
        ThreeNames two = new ThreeNames();
        one.assign(0, "John");
        one.assign(1, "Jane");
        one.assign(2, "Doe");
        two.assign(0, "Jack");
        two.assign(1, "Bean");
        two.assign(2, "Stalk");
        if (one.compareTo(two) == -1){
            System.out.println("Names do not equal.");
        }
        else{
            System.out.println("Names equal!");
        }

        ThreeNames three = new ThreeNames();
        three.assign(0, "John");
        three.assign(1, "Jane");
        three.assign(2, "Doe");
        if (one.compareTo(three) == -1){
            System.out.println("Names do not equal.");
        }
        else{
            System.out.println("Names equal!");
        }
        
        //listofThings();
    }
        

    }
