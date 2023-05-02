public class Playuh {
    private String name;
    private int health = 10;


    public Playuh(String name){
        this.name = name;
    }

    public String getName(){
        return this.name;
    }

    public int decHealth(int dec){
        return this.health -= dec;
    }

    public int getHealth(){
        return this.health;
    }

    @Override
    public String toString() {
        return String.format("%s\nHealth: %d", this.name, this.health);
    }
    
}
