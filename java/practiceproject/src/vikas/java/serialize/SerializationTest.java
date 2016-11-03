package vikas.java.serialize;

import java.io.IOException;

public class SerializationTest {

    public static void main(String[] args) {
        String fileName="employee.bin";
        Employee emp = new Employee();
        emp.setId(100);
        emp.setName("Pankaj");
        emp.setSalary(5000);
        emp.data=99;

        //serialize to file
        try {
            SerializationUtil.serialize(emp, fileName);
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }

        Employee empNew = null;
        try {
            empNew = (Employee) SerializationUtil.deserialize(fileName);
        } catch (ClassNotFoundException | IOException e) {
            e.printStackTrace();
        }

        System.out.println("Emp Object::"+emp);
        System.out.println("EmpNew Object::"+empNew);

    }

}
