package vikas.java.polymorphism;

class Demo{
   public void myMethod(Object obj){
       System.out.println("Second myMethod of class Demo");
   }
   public void myMethod(String s){ 
       System.out.println("String method");
   }
}
class Sample4{
   public static void main(String args[]){
       Demo obj1= new Demo();
       obj1.myMethod(null);
   }
}