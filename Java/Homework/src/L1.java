package Homework.src;

public class L1 {
    public static void main(String args[]){
        /* 
        ThreeThings <Integer> list = new ThreeThings<Integer>(1, 2,3);
        ThreeThings <Integer> list2 = new ThreeThings<Integer>(1, 3,2);
        */
        ThreeThings <String> list = new ThreeThings<String>("Alvin", "Simon", "Theodore");
        ThreeThings <String> list2 = new ThreeThings<String>("Moe", "Larry", "Curly");
        System.out.printf("First List: %s\n", list.toString());
        System.out.printf("Second List: %s", list2.toString());
        if(list.equals(list2)){
            System.out.println("\nLists do equal");
        }
        else{
            System.out.println("\nLists do not equal");
        }

        list.swap(0, 2);
        list.swap(2, 1);
        System.out.printf("\nSWAP:\nFirst List: %s\n", list.toString());

        if(list.equals(list2)){
            System.out.println("\nLists do equal");
        }
        else{
            System.out.println("\nLists do not equal");
        }

    
    
    
    }
}
