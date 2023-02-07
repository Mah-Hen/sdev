public class Card {
    private  int value;
    private char suit;
    private String card;

    public Card(){
        this.value = 0;
        this.suit = ' ';
    }
    public Card(int value, char suit){
        this.value = value;
        this.suit = suit;
    }
     public char getSuit(){
        return suit;
     }

    public void setSuit(char suit){
        this.suit = suit;

    }

    public int getValue(){
        return value;
    }

    public void setValue(int value){
        this.value = value;
    }

    public String getCard(){
        String Vstr = Integer.toString(value);
        String Sstr = ""+ suit;
        card = Vstr+Sstr;

        
        return card;
    }

    public boolean equalSuit (Object obj){
        Card other = (Card)obj;
        if(suit != other.suit)
            return false;
        return true;
    }

    public boolean equalValue (Object obj){
        Card other = (Card)obj;
        if(value != other.value)
            return false;
        return true;
    }
     }

