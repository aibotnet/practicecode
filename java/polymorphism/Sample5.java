class Demo{
   public static void myMethod(float f){
       System.out.println("float");
   }
   public static void myMethod(double  f){ 
       System.out.println("double");
   }
}
class Sample5{
   public static void main(String args[]){
       //Demo obj1= new Demo();
       Demo.myMethod(2);
       Demo.myMethod(2.0);
   }
}