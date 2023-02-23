/* 
Mahlaki Henry
2/8/2022
Homework 5
This is my own original 
*/
public class Main {
    public static void main(String[] args) throws Exception {
        //Person
        Person p1 = new Person("Ed Rooney", "American"); // Principal Ed Rooney
        Person p2 = new Person("Franz Chopin", "Dutch"); // Principal Franz Chopin

        //Schools
        School sc1 = new School("Glenbrook North High School", "Illinois", p1); // School Glenbrook North High School
        School sc2 = new School("Hampton High School", "Virginia", p2); // Hampton High School

        //Students
        Student s1 = new Student("Ferris Bueller", "American",sc1); // Student Ferris Bueller
        Student s2 = new Student("Andie Walsh", "British", sc2); // Student Andie Walsh
        
       
        
        //Print Statements
        System.out.printf("Student, %s is attending,\n%s\n",s1.getName(),sc1.toString()); // Student, {s1} is attending, {sc1}. The principal is {p1} 
        System.out.printf("\nStudent, %s is attending,\n%s\n",s2.getName(),sc2.toString()); //Student {s2} is attending, {sc2}. The principal is {p2}

    }
}
