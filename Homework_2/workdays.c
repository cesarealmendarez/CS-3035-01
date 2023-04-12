/*
    Cesar Almendarez
    CSULA Spring 2023
    CS 3035-01 Programming Paradigms
    Homework 2 (Jagged Arrays and Enumerations)
    -> Q2 Enumerations and Cases in C
    April 5 2023
*/

#include <stdio.h>

// Intialize week enum 
enum week{MON, TUES, WED, THURS, FRI, SAT, SUN};

int main() {

    printf("Enter a day of the week represented as a number 0 - 6.\n");
    printf("0 being Monday, 1 being Tuesday ... 6 being Sunday, etc.\n");

    // Prompt use int input and initalize day
    enum week day;
    scanf("%d", &day);

    // Output 
    switch (day) {
        case MON:
        case TUES:
        case WED:
        case THURS:
        case FRI:
            printf("Its a workday!.\n");
            break;
        case SAT:
        case SUN:
            printf("Its a weekend!.\n");
            break;
        default:
            printf("Invalid input!\n");
    }

    return 0;
}

/*
    ---- Output ----
    Enter a day of the week represented as a number 0 - 6.
    0 being Monday, 1 being Tuesday ... 6 being Sunday, etc.
    -> 0

    Its a workday!.

    Enter a day of the week represented as a number 0 - 6.
    0 being Monday, 1 being Tuesday ... 6 being Sunday, etc.
    -> 6

    Its a weekend!.

    Enter a day of the week represented as a number 0 - 6.
    0 being Monday, 1 being Tuesday ... 6 being Sunday, etc.
    -> 10

    Invalid input!
*/