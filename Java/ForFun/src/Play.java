public class Play {
    public void playBattle(){

    }

    public static void main(String[] args) throws Exception {
        Playuh P1 = new Playuh("John");
        Playuh P2 = new Playuh("Jake");
        Battle b = new Battle(P1, P2);
        Data d = new Data();
        Deck Pile = d.getData();
       

        Deck p1Deck = new Deck();
        Deck p2Deck = new Deck();
        int size = Pile.size();
        int p1Win = 0;
        int p2Win = 0;
        String type = "";

        for (int i=size-1; i>=0; i--){
            Pile.shuffle();
            if (i%2==0){
                p1Deck.addCard(Pile.getCard(i));
                Pile.removeCard(Pile.getCard(i));
            }
            else{
                p2Deck.addCard(Pile.getCard(i));
                Pile.removeCard(Pile.getCard(i));
            }
        }
        int cnt = 1;
        System.out.println("----Game Begins----\n");
        while (true){
            System.out.printf("\n----Round %d----\n", cnt);
            System.out.printf("%s's first card is: %s\n%s's first card is: %s\n",P1.getName(), p1Deck.firstCard(), P2.getName(), p2Deck.firstCard());
            int win = b.baseGame(p1Deck.firstCard(), p2Deck.firstCard());
            if(win > 0){
                p1Win++;
                p2Deck.removeCard(p2Deck.firstCard());
            }
            else{
                p2Win++;
                p1Deck.removeCard(p1Deck.firstCard());
            }

            if ((p1Deck.isEmpty()||p2Deck.isEmpty()) ||(P1.getHealth() == 0 || P2.getHealth() == 0)){
                if(P1.getHealth() == 0 || P2.getHealth() == 0){
                    type = "No Health Left";
                }
                else if(p1Deck.isEmpty()||p2Deck.isEmpty()){
                    type = "No Cards Left";
                }
                break;
            }
            cnt++;
        }
        System.out.println("\n----End----");
        System.out.printf("\nThe game ended by %s", type);
        if(p1Win>p2Win){
            System.out.printf("\n%s Wins the game with %d card(s) left", P1.getName(), p1Deck.size());}
        else{
            System.out.printf("\n%s Wins the game with %d card(s) left", P2.getName(), p2Deck.size());
        }

    }
}
 