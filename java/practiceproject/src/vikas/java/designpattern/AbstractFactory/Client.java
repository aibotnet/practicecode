package vikas.java.designpattern.AbstractFactory;


interface CPU {
    void process();
}

interface CPUFactory {
	CPU produceCPU();
}

class AMDFactory implements CPUFactory {
    public CPU produceCPU() {
        return new AMDCPU();
    }
}

class IntelFactory implements CPUFactory {
    public CPU produceCPU() {
        return new IntelCPU();
    }
}

class AMDCPU implements CPU {
    public void process() {
        System.out.println("AMD is processing...");
    }
}

class IntelCPU implements CPU {
    public void process() {
        System.out.println("Intel is processing...");
    }
}

class Computer {
	CPU cpu;

    public Computer(CPUFactory factory) {
    	cpu = factory.produceCPU();
        cpu.process();
    }
}

public class Client {
    public static void main(String[] args) {
        new Computer(createSpecificFactory());
    }

    public static CPUFactory createSpecificFactory() {
        int sys = 0; // based on specific requirement
        if (sys == 0)
        	return new AMDFactory();
        else
        	return new IntelFactory();
    }
}
