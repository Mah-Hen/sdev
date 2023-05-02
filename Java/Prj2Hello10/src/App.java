public class App {
    public static <T> void main(String[] args) throws Exception {
        Die d1 = new Die(6);
        d1.roll();
        System.out.println(d1.toString());

        Dice dice = new Dice(2, d1);
        dice.getSum();
        System.out.println(dice.toString());
    }
}
