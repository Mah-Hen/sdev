import java.util.Arrays;

public class seq {
    private int start;
    private int increment = 1;
    private int count;

    public seq(int start, int increment, int count){
        this.start = start;
        this.increment = increment;
        this.count = count;

    }

    public int [] getSeq(){
        int cnt = 0;
        int [] L = new int [this.count];
        int x = this.start;

        while (cnt < this.count){
            L[cnt] = x;
            x += this.increment;
            cnt ++;
        }
        
        
        
        return L;
    }

    @Override
    public String toString(){
        return Arrays.toString(getSeq());
    }



}
