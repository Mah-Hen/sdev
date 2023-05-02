package Homework.src;
import java.util.ArrayList;

public class ThreeThings<T> {
    private ArrayList <T> threethings;
    private T thingOne;
    private T thingTwo;
    private T thingThree;


    public ThreeThings(T one, T two, T three){
            this.thingOne = one;
            this.thingTwo = two;
            this.thingThree = three;
            this.threethings = new ArrayList<T>(3);
            threethings.add(thingOne);
            threethings.add(thingTwo);
            threethings.add(thingThree);
            
    }

    
    public void swap(int This, int that){
        T thatEle = threethings.get(that);
        T thisEle = threethings.get(This);

         this.threethings.set(This, thatEle);
         this.threethings.set(that, thisEle);

         if (This == 0) {
            setThingOne(thatEle);
        } else if (that == 0) {
            setThingOne(thisEle);
        }
        if (This == 1) {
            setThingTwo(thatEle);
        } else if (that == 1) {
            setThingTwo(thisEle);
        }
        if (This == 2) {
            setThingThree(thatEle);
        } else if (that == 2) {
            setThingThree(thisEle);
        }
    }


    public T getThingOne() {
        return thingOne;
    }



    public void setThingOne(T thingOne) {
        this.thingOne = thingOne;
    }



    public T getThingTwo() {
        return thingTwo;
    }



    public void setThingTwo(T thingTwo) {
        this.thingTwo = thingTwo;
    }



    public T getThingThree() {
        return thingThree;
    }



    public void setThingThree(T thingThree) {
        this.thingThree = thingThree;
    }



    @Override
    public boolean equals(Object obj) {
        ThreeThings <T> other = (ThreeThings <T>) obj;
        return this.thingOne == other.thingOne && this.thingTwo==other.thingTwo && this.thingThree == other.thingThree;
    }
 

    @Override
    public String toString(){
        String out = "";
        for (T thing: this.threethings){
            out += thing + " ";
        }
        return out;
    }
}
