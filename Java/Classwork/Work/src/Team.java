public class Team implements Biggest{
    private String name;
    private double[] heights;

    private int logicalSize;

    public Team(String name){
        this.name = name;
        this.heights = new double [MAX_SIZE];
        this.logicalSize = 0;
    }
    
    public double max(){
        double theMax = heights[0];
        for (int i = 1; i<logicalSize; i++){
            if(theMax < heights[i]){
                theMax = heights[i];
            }
        }
        return theMax;
    }

    
    public boolean notEmpty(){
        return this.logicalSize > 0;
    }

    public boolean atCapicity(){
        return this.logicalSize == MAX_SIZE;
    }

    public void add(double value){
        heights[logicalSize] = value;
        logicalSize++;
    }

    @Override
    public String toString(){
        String out = this.name;
        for (int i = 0; i<logicalSize; i++){
            out +=  "\n" + this.heights[i];
        }
        return out;
    }
}
