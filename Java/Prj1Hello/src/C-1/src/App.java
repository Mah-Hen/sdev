import java.util.Random;

public class App {
    public static void main(String[] args) throws Exception {
        Lamp [] Lamps = new Lamp[30]; // Empty list of 30 Lamp objects
        Random rand = new Random();
        int index = 0; 
        index = rand.nextInt(30); // random number for flipping the lamps
        System.out.printf("\n%d Lamps will be flipped\n", index);
        int i;

        for(i=0; i<Lamps.length; i++){ 
           Lamps[i] = new Lamp(); // Adds 30 Lamp objects to the empty list
           if(i<index){
            Lamps[i].flip(); // Flips a random amount of Lamps 
           }
           }
        //Print Statements
        System.out.println(" 30 Lamps prior to change:");
        display(Lamps); // Display Lamp list before the change

        System.out.println(); //Extra space
        System.out.printf("\n%d Lamps will be flipped\n", index);
        System.out.println(" 30 Lamps after the change:");
        
        for (int j=0; j<=Lamps.length-1; j++){
            if(j<=9){ 
                Lamps[j].flip();}  // Lamps in indices 10 and below will be flipped
            else if(j<20 && j>=10){ // Lamps in indices 10-20 will turn off
                Lamps[j].turnOff();
            }
            else{
                Lamps[j].turnOn(); // Last set of 10 lamps will be tunred on
            }
        }
        display(Lamps); // Display lamp list after the change
       
    }

    public static void display(Lamp[] arr){
        int count = 0;
        String str = "";
        for (int i=0; i<arr.length;i++){
            count++;
            if(count%5==0){
                str+= arr[i]+"\n";
            }
            else{
                str+= arr[i]+"\t";
            }
            // Printing out the list and potentially the 5ish columns
            }
        System.out.println(str);
        }
    }


