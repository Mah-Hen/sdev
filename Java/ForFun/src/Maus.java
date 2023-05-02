import java.util.Arrays;

public class Maus {
    public static void main(String [] args){
        int alphaLen = 26;
        String quote = "To die, it is easy, but you have to struggle for life!";
        char [] arr = quote.toLowerCase().toCharArray();
        char [] encryptArr = new char [arr.length];

        for (int i=0; i<arr.length;i++){
            char c = arr[i];
            if (Character.isLetter(arr[i])){
                int dist = (((int)arr[i] - 'a' + 19) % alphaLen + alphaLen) % alphaLen + 'a'; // 19 is shift, for parsha truma

                encryptArr[i] = (char)(dist); 
            }
        }
        for (char c:encryptArr){
            System.out.print(c+" ");
        }
        System.out.println("\n- Vladek Spiegelman");

    } 
}
