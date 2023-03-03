/*
    File: Lab6.c
    Authored By: Cesar E Almendarez
    Written On: February 8 2023

    This program will ask the user to enter an 10 integers using a while loop
    In each loop the user's input will be compared to the previous highest grade
    If the user's input is greater that the previous highest grade it's value will be assiged to the highestGrade variable
    At the end the highest grade will be printed
*/

#include <stdio.h>

int main(void) {
    int i = 1;
    int grade;
    
    int highestGrade = 0;
    
    while (i <= 10) {
        printf("Enter Student %d Grade: ", i);
        scanf("%d", &grade);
        
        if(grade > highestGrade) {
            highestGrade = grade;
        }
        
        i++;
    }
    
    printf("\n");
    printf("%d is the highest score by any student \n", highestGrade);
    
    return 0;
}


/*
    Sample Run:

        Enter Student 1 Grade: 80
        Enter Student 2 Grade: 92
        Enter Student 3 Grade: 56
        Enter Student 4 Grade: 83
        Enter Student 5 Grade: 63
        Enter Student 6 Grade: 0
        Enter Student 7 Grade: 98
        Enter Student 8 Grade: 2
        Enter Student 9 Grade: 75
        Enter Student 10 Grade: 55
 
        98 is the highest score by any student
*/


