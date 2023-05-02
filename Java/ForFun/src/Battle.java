import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class Battle {
    Random rand = new Random();
    Playuh player1;
    Playuh player2;
    public Battle(Playuh P1, Playuh P2){
       this.player1 = P1;
       this.player2 = P2;
    }

    public Map<String, Integer> withEffects(Card p1, Card p2){
        int P1xAtk; // extra attack by lowering oppositions defense
        int P2xAtk;
        int P1xdef; // extra defense by lowering oppositions attack
        int P2xdef;
        Map <String, Integer> tuple = new HashMap <>();

        if (p1.getEffect().equals("Darkness")){
            P1xAtk = rand.nextInt(p1.getDefense()-1); //kinda like a multiplier but instead of multiplring it just increments
            tuple.put("P1Atk", P1xAtk);
        }
        if (p2.getEffect().equals("Darkness")){
            P2xAtk =  rand.nextInt(p2.getDefense()-1); //kinda like a multiplier but instead of multiplring it just increments
            tuple.put("P2Atk", P2xAtk);
        }


        if (p1.getEffect().equals("Venom")){
            P1xdef = rand.nextInt(p1.getAttack()-1);
            tuple.put("P1def", P1xdef);
        }
        if (p2.getEffect().equals("Venom")){
            P2xdef = rand.nextInt(p2.getAttack()-1);
            tuple.put("P2def", P2xdef);
        }  
        

        if(p1.getEffect().equals("Magic")){
            int choice = rand.nextInt(2); // If choice is 1 then attack, otherwise defend
            if (choice==1){
                P1xAtk = rand.nextInt(p1.getDefense());
                tuple.put("P1Atk", P1xAtk);
            }
            else{
                P1xdef = rand.nextInt(p1.getAttack());
                tuple.put("P1def", P1xdef);
            }
        }


        if(p2.getEffect().equals("Magic")){
            int choice = rand.nextInt(2);
            if (choice==1){
                P2xAtk = rand.nextInt(p2.getDefense());
                tuple.put("P2Atk", P2xAtk);
            }
            else{
                P2xdef = rand.nextInt(p2.getAttack());
                tuple.put("P2def", P2xdef);
            }
        }


        if (p1.getEffect().equals("Burn")){
            P1xdef = rand.nextInt(p1.getAttack()-1);
            tuple.put("P1def", P1xdef);
        }
        if (p2.getEffect().equals("Burn")){
            P2xdef = rand.nextInt(p2.getAttack()-1);
            tuple.put("P2def", P2xdef);
        }  

        return tuple;
    }

    public int baseGame(Card p1Card, Card p2Card){
        Map <String, Integer> tuple = withEffects(p1Card, p2Card);

        if (tuple.containsKey("P1def")){ // Extra defense by lowering the opposition's attack
            int multi = tuple.get("P1def");
            p2Card.setAttack(p2Card.getAttack()-multi); // Subtract the base attack by the effect multiplier
        }
        if (tuple.containsKey("P2def")){
            int multi = tuple.get("P2def");
            p1Card.setAttack(p1Card.getAttack()-multi);
        }
        if(tuple.containsKey("P1Atk")){ // Extra attack by lowering the opposition's defense
            int multi = tuple.get("P1Atk");
            p2Card.setDefense(p2Card.getDefense()-multi);
        }
        if(tuple.containsKey("P2Atk")){
            int multi = tuple.get("P2Atk");
            p1Card.setDefense(p1Card.getDefense()-multi);
        }


        if (!(p1Card.getAttack() > p2Card.getAttack())){
            int damage = p2Card.getAttack() - p1Card.getDefense();
            System.out.printf("%s's %s defeats %s's %s.\n", player2.getName(), p2Card.getName(), player1.getName(), p1Card.getName());
            if (damage > 0){
                player1.decHealth(damage);
                System.out.printf("\n%s lost %d health\n", player1.getName(), damage);
            }
                return -1; // -1 Player 2 wins; 1 Player 1 wins
        } 
        if(p1Card.getAttack() == p2Card.getAttack()){
            if (p1Card.getDefense() > p2Card.getDefense()){
                System.out.printf("%s's %s defeats %s's %s.\n", player1.getName(), p1Card.getName(), player2.getName(), p2Card.getName());
                return 1;
            }
            else{
                System.out.printf("%s's %s defeats %s's %s.\n", player2.getName(), p2Card.getName(), player1.getName(), p1Card.getName());
                return -1;
            }
        }
        else{
            int damage = p1Card.getAttack() - p2Card.getDefense();
            System.out.printf("%s's %s defeats %s's %s.\n", player1.getName(), p1Card.getName(), player2.getName(), p2Card.getName());
            if (damage > 0){
                player2.decHealth(damage);
                System.out.printf("\n%s lost %d health\n", player2.getName(), damage);
            }
                return 1; // -1 Player 2 wins; 1 Player 1 wins
        }
    }
}
