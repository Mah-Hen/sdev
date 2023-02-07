public class Student extends Person {
    private String school;

    public Student(String name, String citizenship, String school){
        super(name, citizenship); // a call to the parent's constuctor
        this.school = school;
    }

    public void setSchool(String school){
        this.school = school;
    }

    @Override
    public String toString(){
        return String.format("%s and attends %s", super.toString(), school); // a call to the parent's toString method
    }

    @Override
    public boolean equals(Object obj){
        if (obj != null && obj.getClass() == getClass()){
            if (obj instanceof Student){
                return super.equals(obj) && school == ((Student)obj).school;
            }
        }
        return false;
    }
}
