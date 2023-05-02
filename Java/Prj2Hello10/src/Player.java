public class Player implements Craps{
    private int winnings = Craps.winnings;
    private String name;

    public Player(String name){ // Modify constructor to either have no String name or either just have to modify Main code
        this.name = name;
    }

    private static void wait(int ms){
        try
        {
            Thread.sleep(ms);
        }
        catch(InterruptedException ex)
        {
            Thread.currentThread().interrupt();
        }
    }

    public String getName(){
        return this.name;
    }

    public void setName(String name){
        this.name = name;
    }

    public int getWinnings(){
        return this.winnings;
    }

    public void incWinnings(int bet){
        this.winnings += bet;
    }

    public void decWinnings(int bet){
        this.winnings -= bet;
    }

    
    public Boolean Bet(String betType, Dice dice, int roll){
        Boolean win = false;

        if (betType.toLowerCase().equals("pass")){
    
            if (roll == 7|| roll == 11){
                win = true;
            }
            else if (roll == 2 || roll == 3 || roll == 12){
                win = false;
            }
            else{
                wait(1000);
                System.out.println("\nPoint ROUND!");
                System.out.println("---------------\n");
                int newRoll = 0;
                while(!(win)){
                    newRoll = dice.getSum();
                    System.out.printf("Shooter rolls %d\n", newRoll);
                    wait(1000);
                    if((newRoll != roll)){
                        if (newRoll == 7){
                            System.out.println("Point MISSED!");
                            wait(1000);
                            break;
                            }
                        else{
                            System.out.println("Retry!");
                            continue;
                        }
                    }
                    else{
                        System.out.println("Point SCORED!");
                        wait(1000);
                        win = true; // Hopefully while loop breaks here
                        break;
                    }
                    
                }
            }
        }
        else if (betType.toLowerCase().equals("field")){
            if (roll == 2 || roll == 3 || roll == 4 || roll == 9 || roll == 10 || roll == 12) {
                win = true;
            }
        }


        return win;
    }

    @Override
    public String toString(){
        return String.format("Player %s has %d chips", this.name, this.winnings);
    }


}
