public class App2 {
    public static void main(String[] args) throws Exception {
       Card Spade10 = new Card(10, 'S');
       Card Club10 = new Card(10, 'C');
       System.out.println("First card is:");
       System.out.print(Spade10.getCard());
       System.out.printf("\nSecond card is:\n");
       System.out.println(Club10.getCard());
       if(Club10.equalSuit(Spade10)){
        System.out.println("These cards have equal suits.");
        }
        else{
            System.out.println("These cards do not have equal suits.");
        }

        if(Club10.equalValue(Spade10)){
            System.out.println("These cards have equal value.");
        }
        else{
            System.out.println("These cards do not have equal value.");
        }
    }
}
