class ABC{
   public void disp()
   {
      System.out.println("disp() method of parent class");
   }
   public void abc()
   {
      System.out.println("abc() method of parent class");
   }	   
}
class Test extends ABC{
   public void disp(){
      System.out.println("disp() method of Child class");
   }
   public void xyz(){
      System.out.println("xyz() method of Child class");
   }
   public static void main( String args[]) {
      //Parent class reference to child class object
      ABC obj = new Test();
      obj.disp();
      obj.abc();
      obj.xyz();
   }
}