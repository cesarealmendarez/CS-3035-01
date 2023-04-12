/*
    Cesar Almendarez
    CSULA Spring 2023
    CS 3035-01 Programming Paradigms
    Homework 2 (Jagged Arrays and Enumerations)
    -> Q1 Jagged Arrays in Java
    April 5 2023
*/

package main;

import java.util.Random;
import java.util.Scanner;

public class JaggedArray {

	public static void main(String[] args) {
	 
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the number of rows: ");
        
        int rows = scanner.nextInt();
        
        // Declare 2D array 
        int[][] jaggedArray = new int[rows][];
        
        Random random = new Random();

        // Populate 2D array with random ints
        for(int i = 0; i < rows; i++){
        	int columns = random.nextInt(10);
        	
            jaggedArray[i] = new int[columns];
            
            for(int j = 0; j < columns; j++){
            	jaggedArray[i][j] = j + 1;
            }
        }
        
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < jaggedArray[i].length; j++){
                System.out.print(jaggedArray[i][j] + " ");
            }
            
            System.out.println();
        }	
	}
}

//--- Output 1 ---
//Enter the number of rows: 12
//1 2 3 
//1 2 3 4 5 
//1 
//
//1 
//1 2 3 4 5 6 
//1 2 3 4 5 6 7 
//1 2 3 4 5 6 7 8 
//1 
//1 2 3 
//1 2 3 4 
//1 2 3 4 5 6 7 8 9 

//--- Output 2 ---
//Enter the number of rows: 2
//1 
//1 2 3 4 5 