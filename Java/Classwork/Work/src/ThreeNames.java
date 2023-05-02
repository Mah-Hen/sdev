public class ThreeNames implements Comparable<ThreeNames>{
    private String[] list;
    private boolean[] occupied = {false, false, false};

    public ThreeNames(){
        this.list = new String[3];
        list[0] = list[1] = list[2] = "";

    }

    public void assign (int pos, String name){
        if (validIndex(pos)){
            this.list[pos] = name;
            this.occupied[pos] = true;
        }
    }

    public boolean validIndex(int pos){
        return pos >= 0 && pos < 3;
    }

    public String getName(int pos){
        return this.list[pos];
    }

    @Override
    public int compareTo(ThreeNames objNames){ 
        if (this.getName(0).equals(objNames.getName(0))){
            if (this.getName(1).equals(objNames.getName(1))){
                if(this.getName(2).equals(objNames.getName(2))){
                    return 1;
                }
            }
        }

        return -1;
        
    }


    @Override
    public String toString(){
        String out = "";
        for(int i = 0; i < 3; i++){
            out += i + ":";
            if (this.occupied[i])
                out += String.format("%-10s  ", this.list[i]) + "  ";
            else
                out += String.format("%-10s   ", "-----") + "  ";
            
        }
        return out;
    }

   
}

