/*
    File: Lab5.c
    Authored By: Cesar E Almendarez
    Written On: February 6 2023

    This program will ask the user to enter an integer using the printf() method.
    Their integer will then be stored in the int variable userInt
    If userInt % 2 results in a remainder of 0, then userInt is even
    Else if userInt % 2 results in a remainder other than 0, then userInt is odd
*/

#include <stdio.h>

int main( void ) {
    int userInt;

    printf("Please enter an integer: ");

    scanf("%d", &userInt);

    if(userInt % 2 == 0) {
        printf("%d is even \n", userInt);
    } else {
        printf("%d is odd \n", userInt);
    }

    return 0;
}

/*
    Sample Runs:

    Please enter an integer: 5
    5 is odd 

    Please enter an integer: -2
    -2 is odd 
*/

