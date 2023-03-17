package main;

public class John {
	// These methods can be directly accessed from another class
	public void MowLawn(String neighbor) {
		System.out.println("John is mowing " + neighbor + "'s lawn.");
	}
	
	public void FixCar(String neighbor, String carModel) {
		System.out.println("John is fixing " + neighbor + "'s " + carModel);
	}
	
	public void PaintHouse(String neighbor) {
		System.out.println("John is painting " + neighbor + "'s house.");
	}
	
	// These methods cannot be directly accessed from another class
	private void Laundry() {
		System.out.println("John is doing laundry");
	}
	
	private void Cook(String food) {
		System.out.println("John is cooking " + food);
	}
	
	private void Research() {
		System.out.println("John is researching");
	}
	
	// Private methods can now be accessed via this public method
	public void PrivateTasks() {
		Laundry();
		Cook("Ratatouille");
		Research();
	}
}
