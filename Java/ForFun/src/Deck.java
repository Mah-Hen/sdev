import java.util.ArrayList;
import java.util.Collections;

public class Deck{
    private ArrayList<Card> cards;

    public Deck(){
        this.cards = new ArrayList<>();
    }

    public void addCard(Card card){
        cards.add(card);
    }

    public void removeCard(Card card){
        cards.remove(card);
    }

    public Card firstCard(){
        return cards.get(0);
    }

    public Card getCard(int idx){
        return cards.get(idx);
    }

    public Boolean isEmpty(){
        return cards.size() == 0;
    }

    public void shuffle(){
        Collections.shuffle(cards);
    }

    public int size(){
        return cards.size();
    }

    public String toString(){
        String out = "";
        for (int i=0; i<cards.size();i++){
            Card card = getCard(i);
            out += String.format("%s\nAtk: %d\tDef: %d\n",card.getName(), card.getAttack(), card.getDefense());
            if (i<cards.size()-1){
                out += "\n";
            }
            else{
                out += "";
            }
        }
        return out;
    } 
}
