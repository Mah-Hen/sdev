import java.util.Scanner;


public class Game implements User{
    

    public static void clear() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    private static void wait(int ms) {
        try {
            Thread.sleep(ms);
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
    }

    public static String Quit(Scanner in) {
        String inp = "";
        clear();
        while (true) {
            System.out.println("Enter 'On' to Quit\nOr 'Off' to Play");
            inp = in.nextLine().toLowerCase();
            if (inp.isEmpty()) {
                System.out.println("Error! Enter String");
            } else if (inp.equalsIgnoreCase("off")) {
                break;
            } else if (inp.equalsIgnoreCase("on")) {
                break;
            } else {
                System.out.println("Error!");
            }

        }

        return inp;
    }

    public String getName(Scanner in) {
        clear();
        while (true) {
            System.out.println("Please enter your name: ");
            String name = in.nextLine();
            if (name.isEmpty()) {
                System.out.println("Error! Enter a String");
                continue;
            }
            if (name.matches("[a-zA-Z]+")) {
                return name;
            } else {
                System.out.println("Error!");
                continue;
            }
        }
    }

    public String getBetType(Scanner in){
        String type = "";
        clear();
        while (true){
            System.out.println("There are two betting option you can choose. Pass Line and Field Bet.\nIf you want more information, enter 'I'.");
            System.out.println("Or, enter (Pass) for Pass Line or (Field) for Field Bet: ");
            type = in.nextLine();
            clear();
            if (!(type.matches("[a-zA-Z]+"))){
                System.out.println("Error! Not a bet type.");
                wait(1500);
                clear();
                continue;
            }
            else{
                if (type.toLowerCase().equals("field") || type.toLowerCase().equals("pass")){
                    break;
                }
                if (type.toLowerCase().equals("i")){
                    displayInfo();
                    wait(3000);
                    clear();
                    continue;
                }
            }
        }

        return type;
    }

    public int getBet(Player P1, Scanner in, String betType) {
        int bet = -1; // flag

        while (true) {
            clear();
            System.out.printf("-------%s ROUND-------", betType.toUpperCase());
            System.out.println("\n"+P1.toString()); // P1.getwinnings
            System.out.println("\nEach bet is either 0, 5, 10, 15, or 20 chips.");
            System.out.println("Enter quit to leave");
            System.out.println("Or, enter the bet you want to place: ");
            String input = in.nextLine();
            if (!(input.matches("\\d+"))) {
                if (input.toLowerCase().equals("quit")) {
                    clear();
                    break;
                }
                clear();
                System.out.println("Error! Invalid Bet.");
                wait(1500);
                continue;
            } else {
                bet = Integer.parseInt(input);
                if (!(bet == 0 || bet == 5 || bet == 10 || bet == 15 || bet == 20)) {
                    clear();
                    System.out.println("Error! Invalid Bet.");
                    wait(1500);
                    continue;
                } else {
                    if (bet > P1.getWinnings()){
                        clear();
                        System.out.println("Not Enough Chips.");
                        wait(1500);
                        continue;}
                    else{
                        return bet;
                    }
                }
            }
        }

        return bet;
    }

    public static void displayInfo(){
        clear();
        System.out.print("For \"Pass Line\" option: The person rolling the dice is known as the \"shooter,\" and the shooter's roll is  called the \"come-out roll.\" On the come-out roll, the shooter's goal is to roll a 7 or an 11. You win.\nIf the shooter rolls a 2, 3, or 12, known as \"craps,\" you lose."
        + "\nIf the shooter rolls any other number, that number becomes the \"point.\" The shooter then continues rolling the dice until they either roll the point again (in which case they win) or roll a 7 (in which case they lose)."
        + "\nFor \"Field Bet\" option: The person rolling the dice is known as the \"shooter.\"\nThe shooter's goal is to roll once on either a 2, 3, 4, 9, 10, 11, or 12 to win. Anything else you lose.");
        wait(15000);
    }

    public static void displayIntro(){
        clear();
         System.out.println("\t--Welcome to the Game of Craps--\nCraps is a fast-pasced, dice game that's played with 2 6-sided dice which are numbered from 1 to 6.\nThe sum of those dice are what you're wagering on."
        +"\n\t\t-ENJOY!-"); 
        wait(5000);    
    }

    public static void displayQuit(Player P1) {
        clear();
        System.out.printf("Player %s is leaving the table with %d chips", P1.getName(), P1.getWinnings());
    }

    public static void main(String[] args) throws Exception {
        User craps = new Game();
        Player P1 = new Player("");
        Scanner in = new Scanner(System.in);
        Die d1 = new Die(6);
        Dice dice = new Dice(2, d1);

        String name = craps.getName(in);
        P1.setName(name);
        String Decision = Quit(in);
       

        

        if (Decision.equals("off")) {
            
            //displayIntro();
            String type = craps.getBetType(in);
            while (true) {
                int bet = craps.getBet(P1, in, type);
                if (bet == -1){
                    break;
                }
                int roll = dice.getSum();

                clear();
                System.out.printf("Shooter rolls a %d\n", roll);
                Boolean win = P1.Bet(type, dice, roll);
                wait(2000);
                if (win) {
                    clear();
                    System.out.printf("Player %s Wins %d!", P1.getName(), bet); // P1.getwinnings
                    wait(1500);
                    P1.incWinnings(bet); // P1.getwinnings
                }
                else if (!(win)) {
                    if (type.toLowerCase().equals("pass")) {
                        clear();
                        System.out.printf("CRAPS! Player %s Loses %d!", P1.getName(), bet); // P1.getwinnings
                        P1.decWinnings(bet);
                        wait(2000);
                    }
                    else if(type.toLowerCase().equals("field")){
                        clear();
                        System.out.printf("UH OH! Player %s Lose %d!", P1.getName(), bet); // P1.getwinnings
                        P1.decWinnings(bet);; // P1.getwinnings
                        wait(1500);
                    }
                }
                if (P1.getWinnings() <= 0) { // P1.getwinnings
                    clear();
                    System.out.printf("Player %s's Bankrupt!", P1.getName());
                    wait(1500);
                    break;
                }
            }
        }

        displayQuit(P1); 
        in.close();
        
    }
}
