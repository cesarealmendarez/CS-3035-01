/*
    Assignment: Homework 1
    File: Homework1.c
    Authored By: Cesar E Almendarez
    Written On: February 15 2023
*/

#include <stdio.h>

int yearsBetween(int year1, int year2) {
    /*
        If year1 is greater than year2, year1 will be subtracted from year2
        Else if year2 is greater than year1, year2 will be subtracted from year1
        The difference will be returned
    */
    if(year1 > year2) {
        return year1 - year2;
    } else {
        return year2 - year1;
    }
}

int main(void) {
    // Declare year variables to be assigned via scanf()
    int year1;
    int year2;
    
    // Prompt the user to input 2 year values consecuively
    printf("Please enter a year: ");
    scanf("%d", &year1);
    
    printf("Please enter another year: ");
    scanf("%d", &year2);
    
    // Print the return value of yearsBetween(year1, year2)
    printf("\n%d years between %d and %d \n", yearsBetween(year1, year2), year1, year2);

    return 0;
}


/*
    Sample Runs:
 
        Please enter a year: 2023
        Please enter another year: 2001

        22 years between 2023 and 2001
 
 
        Please enter a year: 2003
        Please enter another year: 2010

        7 years between 2003 and 2010
*/
