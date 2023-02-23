/* 
Mahlaki Henry
2/8/2022
Homework 5
This is my own original 
*/
public class Student extends Person {
    private String name = super.getName();
    private School school;

    public Student(String name, String citizenship, School school){
        super(name, citizenship); // a call to the parent's constuctor
        this.school = school;
    }

    public String getName(){
        return name; 
    }

    public void setName(String name){
         this.name = name;
    }

    public School getSchool() {
        return school;
    }
    
    public void setSchool(School school){
        this.school = school;
    }

    @Override
    public String toString(){
        return String.format("%s and attends %s", super.toString(), school); // a call to the parent's toString method or even to the parent's methods
    }

    @Override
    public boolean equals(Object obj){
        if (obj != null && obj.getClass() == getClass()){
            if (obj instanceof Student){
                // School other = (School) obj;
                //return super.equals(other) && school.equals(other.school) // comparing the parent class equal with the obj in argument and the school
                return super.equals(obj) && school == ((Student)obj).school;
            }
        }
        return false;
    }

}
