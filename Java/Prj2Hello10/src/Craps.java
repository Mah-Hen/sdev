public interface Craps {
    final int winnings = 50;
    Boolean Bet(String betType, Dice die, int roll);
    int getWinnings();
    void decWinnings(int amount);
    void incWinnings(int amount);
}
    /* 
     PassLine is betting on the 'shooter' or the person rolling the dice. If he wins we all win and vice versa. 
     If the shooter rolls a 7 or 11 we win. If he rolls a 2, 3, or 12 we lose. Anything else (1, 4, 5, 6, 8, 9 , 10) 
     is a point, where he shooter then continues rolling the dice until they either roll the point again (in which case they win) 
     or roll a 7 (in which case they lose). If the shooter manages to roll the point again before rolling a 7, 
     all the players who have placed bets on the Pass Line win. If the shooter rolls a 7 before rolling the point again, 
     all the players who have placed bets on the Pass Line lose. 

     Field Bets are one-roll bets that pay out if the shooter rolls a 2, 3, 4, 9, 10, 11, or 12. If the shooter rolls any other number, you lose.

     On the table will be the bet you lay on the table 
     In the pocket is the money (50-+bets) not being betted yet.
    */

