package main;

public class MainJohn {

	public static void main(String[] args) {
		// Create an instance of the John class		
		John john = new John();
		
		// Call the publicly available methods in John
		john.MowLawn("Steven");
		john.FixCar("Buck", "Ford F150");
		john.PaintHouse("Lauren");

		// Call the private methods in John via public method
		john.PrivateTasks();
	}

}
