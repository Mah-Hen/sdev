import java.util.Random;

public class Die {
    private int sides;
    private int [] die; 
    private Random random;
    private int roll;

    public Die(int sides){
        this.sides = sides;
        this.die = new int [sides];
        this.random = new Random();
        for (int i = 0; i<sides; i++){
            this.die[i] = i+1;
        }
        
    }


    public int roll() {
        this.roll = this.random.nextInt(this.sides)+1;
        return this.roll;
    }

    @Override
    public String toString(){
        return "Roll is " + this.roll;

}


}
