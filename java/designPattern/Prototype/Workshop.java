class Bike implements Cloneable {
	private int gears;
	private String bikeType;
	private String model;

  public Bike() {
		bikeType = "Standard";
		model = "Leopard";
		gears = 4;
	}
  
  public Bike clone() {
		return new Bike();
	}
  public void makeAdvanced() {
		bikeType = "Advanced";
		model = "Jaguar";
		gears = 6;
	}
	public String getModel(){
		return model;
	}
}

public class Workshop {
	public Bike makeJaguar(Bike basicBike) {
		basicBike.makeAdvanced();
		return basicBike;
	}
	public static void main(String args[]){
		Bike bike = new Bike();
		Bike basicBike = bike.clone();
		Workshop workShop = new Workshop();
		Bike advancedBike = workShop.makeJaguar(basicBike);
		System.out.println("Prototype Design Pattern: "+advancedBike.getModel());
	}
}
