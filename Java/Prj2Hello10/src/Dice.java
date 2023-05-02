
public class Dice{
    private int [] rollList; // dice list
    private int numDice;
    private int sum;
    private Die d; 

    public Dice(int num, Die d){
        this.d = d;
        this.rollList = new int [num];
        this.numDice = num;
        
    }


    private void findSum() {
        this.sum = 0;
        for(int i = 0; i<this.numDice; i++){
            int roll = d.roll();
            this.rollList[i] = roll;
            this.sum += roll;
        }
    }

    public int getSum(){
        findSum();
        return this.sum;
    }

    private String getRolls(){
        String out = "";
        for(int i = 0; i<this.rollList.length; i++){
            out+= "(" + this.rollList[i] + ")";
        }
        return out;
    }

    @Override
    public String toString(){
       return String.format("Roll is %s with sum %d", getRolls(), this.sum);

}
}
