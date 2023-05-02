public class Card {
    private String name;
    private String type;
    private String effect;
    private int attack;
    private int defense;


    public Card(String name, int attk, int defense, String effect){
        this.name = name;
        this.attack = attk;
        this.defense = defense;
        this.type = "Physical";
        this.effect = effect;
    }

    public Card(String name, String type){
        this.name = name;
        this.type = type;
    }

    public String getName() {
        return name;
    }


    public String getType() {
        return type;
    }


    public String getEffect() {
        return effect;
    }

    public void addEffect(String effect){
        this.effect = effect;
    }


    public int getAttack() {
        return attack;
    }

    public void setAttack(int atk){
        this.attack = atk;
    }


    public int getDefense() {
        return defense;
    }

    public void setDefense(int def){
        this.defense = def;
    }

    @Override
    public String toString() {
        if (this.effect.equals("None")){
            return String.format("\nName: %s\nAtk: %d\tDef:%d", this.name, this.attack, this.defense); 
        }
        else{
            return String.format("\nName: %s\tEffect: %s\nAtk: %d\tDef: %d", this.name, this.effect, this.attack, this.defense);
        }
    }
    
}
