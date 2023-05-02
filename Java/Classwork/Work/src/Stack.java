import java.util.ArrayList;
import java.util.Arrays;

public class Stack<T> {
    private ArrayList<T> index;

    public Stack(){
        this.index = new ArrayList<T>(); // Generic data type
    }

    public int length(){
        return this.index.size();
    } 

    public void push(T item){
        this.index.add(0, item);
    }

    public T peek(){
        try{
            return this.index.get(0);
         }
         catch(IndexOutOfBoundsException error){
            error.printStackTrace();
         }
        return null;
    }

    public T pop(){
        try{
            return this.index.remove(0);
         }
         catch(IndexOutOfBoundsException error){
            error.printStackTrace();
         }
        return null;
}

    @Override
    public String toString(){
        String out = "";
        for(T ele: this.index){
            out += ele.toString();
        }
        return out;
    }
}
