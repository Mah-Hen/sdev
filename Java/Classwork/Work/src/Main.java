public class Main {
    public static void main(String[] args) throws Exception {
        Person AmAmir = new Person("Amiri", "American");
        System.out.println(AmAmir.toString());
        Person BriBrit = new Person("Brittany", "British");
        System.out.println(BriBrit.toString());
        if(AmAmir.equals(BriBrit)){
            System.out.println("These people are equal");
        }
        else{
            System.out.println("These people are not equal");
        }
        Student Amir = new Student("Amir", "American", "America High school");
        System.out.println(Amir.toString());
        Student Brittany = new Student("Brittany", "British", "America High school");
        System.out.println(Brittany.toString());
        if(Amir.equals(Brittany)){
            System.out.println("These students are equal");
        }
        else{
            System.out.println("These students are not equal");
        }
    }
}
