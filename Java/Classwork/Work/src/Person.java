public class Person{
    private String name;
    private String citizenship;

    public Person(String name, String citizenship){
        this.name = name;
        this.citizenship = citizenship;
    }

    public String getName(){
        return name;
    }

    public String getCitizenship(){
        return citizenship;
    }

    public void setName(String name){
        this.name = name;
    }
    public void setCitizenship(String citizenship){
        this.citizenship = citizenship;
    }

    @Override
    public boolean equals(Object obj){
       Person other = (Person) obj;
       if(other.getName().equals(this.getName()) && other.getCitizenship().equals(this.getCitizenship())) {
        return true;
       }
       return false;
    } 

    @Override
    public String toString(){
        return String.format("%s is %s", name, citizenship);
    }
}