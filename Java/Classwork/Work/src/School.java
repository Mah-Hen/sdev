/* 
Mahlaki Henry
2/8/2022
Homework 5
This is my own original 
*/
public class School {
    private String name = "No School";
    private String state = "Invalid";
    private Person principal;

    public School(String name, String state, Person principal){
        this.name = name;
        this.state = state;
        this.principal = principal;
    }

    public String getName() {
        return name;
    }

    public String getState() {
        return state;
    }

    public Person getPrincipal() {
        return principal;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setState(String state) {
        this.state = state;
    }

    public void setPrincipal(Person principal) {
        this.principal = principal;
    }

     @Override
     public String toString(){
        return String.format("%s, %s.\nThe Principal there is %s.", name, state, principal.getName());
     }   
}
