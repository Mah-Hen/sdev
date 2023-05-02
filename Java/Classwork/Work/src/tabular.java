public interface tabular {
    int getNumRows();
    int getNumCols();
    void setXY(int cols, int rows);
    String getXY(int cols, int rows);
    String [][] getCopy();
    void clear();
    boolean isEmpty();
}
