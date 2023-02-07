import java.util.Arrays;
import java.lang.Math;

public class lab1 {
    public static void main(String[] args) throws Exception {
    double [] listX = new double [21];
    int i;

    for (i = 0; i<listX.length; i++){
        listX[i] = (i*0.5); 
    }
    double [] listY = computeVals(listX);

    System.out.print(Arrays.toString(listX));
    System.out.println();
    Display(listY);
    }
    
    public static double [] computeVals(double[] listX){
        double [] listY = new double [21]; 
        int i;
        for (i = 0; i<listX.length; i++){
            Double sqr = listX[i]*listX[i];
            listY[i] = (Math.sin(listX[i])+Math.sin(sqr));

        }

        return listY;
    }

    public static void Display(double [] listY){
        for (int i = 0; i<listY.length; i++){
            System.out.printf("%7.2f\n",listY[i]);
    }


    }
}

