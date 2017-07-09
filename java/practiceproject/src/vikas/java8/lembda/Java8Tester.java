package vikas.java8.lembda;

public class Java8Tester {
	   public static void main(String args[]){
		   
		try {
			String s = "Attachment 101 - Network Usage Charges";
			if (s.matches("Attachment \\d")){
				System.out.print("okkk");
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	   }
	}
