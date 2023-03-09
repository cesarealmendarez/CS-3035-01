/*
    Cesar Almendarez
    CSULA Spring 2023
    CS 3035-01 Programming Paradigms
    Lab 14 (malloc() and free()) 
    March 8 2023
*/

#include <stdio.h>

int main() {
    // Initialize string array with a fixed max size of 5
    char zoo[5][50] = {"Zebra", "Lion", "Elephant", "Turtle", "Gorilla"};

    printf("Animals in Fixed Zoo: \n");

    // Print fixed array's elements
    for(int i = 0; i < 5; i++) {
        printf("%s\n", zoo[i]);
    }

    return 0;
}

// Sample Output

// Animals in Fixed Zoo: 
// Zebra
// Lion
// Elephant
// Turtle
// Gorilla
