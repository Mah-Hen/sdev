import java.util.Scanner;

public interface User {
    String getName(Scanner in);
    String getBetType(Scanner in);
    int getBet(Player P1, Scanner in, String betType);
}
