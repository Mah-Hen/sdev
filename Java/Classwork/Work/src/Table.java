public class Table implements tabular{
    private String[][] tab; 
    private int rows;
    private int cols;

    public Table(int cols, int rows){
        this.rows = rows;
        this.cols = cols;
        this.tab = new String[rows][cols];
        for (int col=0; col<this.cols; col++){
            for (int row=0; row<this.rows; row++){
                this.tab[col][row] = ".";
            } 
            }
    }

    public int getNumRows(){
        return this.rows;
    }

    public int getNumCols(){
        return this.cols;
    }
    
    public void setXY(int cols, int rows){
        this.cols = cols;
        this.rows = rows;
    }
    
    public String getXY(int cols, int rows){
        return this.tab[cols][rows];
    }
    
    public String [][] getCopy(){
        String [][] copyofTab = new String[rows][cols];
        for (int col=0; col<this.cols; col++){
            for (int row=0; row<this.rows; col++){
                copyofTab[col][row] = this.tab[col][row];
            }
        }
        return copyofTab;
    }

    public void clear(){
        for (int col=0; col<this.cols; col++){
            for (int row=0; row<this.rows; row++){
            this.tab[col][row] = ".";
            } 
        }
    }

    public boolean isEmpty(){
        for (int col=0; col<this.cols; col++){
            for (int row=0; row<this.rows; row++){ 
                if(this.tab[col][row] != "."){
                    return false;
                }
        }
    }
    return true;
    }

    @Override
    public String toString(){
        String out = "";
        for (int col=0;col<this.cols;col++){
            for(int row=0;row<this.rows;row++){
                out += this.tab[col][row];
                if (row==4){
                    out+= "\n";
                }
            }
        }
        return out;
    }
}

