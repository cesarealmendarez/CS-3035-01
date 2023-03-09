/*
    Cesar Almendarez
    CSULA Spring 2023
    CS 3035-01 Programming Paradigms
    Lab 13 (Call by Referencing) 
    March 8 2023
*/

#include <stdio.h>

// swap() will reassign X with Y using variable references (*)
void swap(int *X, int *Y) {
    int xtemp = *X;
    *X = *Y;
    *Y = xtemp;
}

int main(void) {

    // Declare and assign wrong int values to X and Y
    int X = 9;
    int Y = 4;
    
    printf("Incorrect Custom Orders: \n John - %d Pizzas \n Marry - %d Pizzas \n", X, Y);

    printf("\n");

    printf("Performing Swap...\n");

    printf("\n");

    // Perform swap() with X and Y as int parameters
    // & Retrieves the reference address
    swap(&X, &Y);

    printf("Correct Customer Orders: \n John - %d Pizzas \n Marry - %d Pizzas \n", X, Y);

}

// Sample Output

// Incorrect Custom Orders: 
//     John - 9 Pizzas 
//     Marry - 4 Pizzas 

// Performing Swap...

// Correct Customer Orders: 
//     John - 4 Pizzas 
//     Marry - 9 Pizzas 
