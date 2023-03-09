/*
    Cesar Almendarez
    CSULA Spring 2023
    CS 3035-01 Programming Paradigms
    Lab 14 (malloc() and free()) 
    March 8 2023
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int capacity;

    // Prompt use for int capacity until a value greater than 4 is entered
    do {
        printf("Enter a capacity, greater than 4, for the dynamic zoo: ");
        scanf("%d", &capacity);
    } while(capacity <= 4);

    // Dyanmically allocate memory for all capacity int elements
    char** zoo = (char**)malloc(capacity * sizeof(char*));

    for(int i = 0; i < capacity; i++) {
        zoo[i] = (char*)malloc(100 * sizeof(char));
    }

    // Assign first three and last elements
    zoo[0] = "Monkey";
    zoo[1] = "Tiger";
    zoo[2] = "Gorilla";
    zoo[capacity - 1] = "Komodo Dragon";

    // Print dynamic array's first three elements
    for(int i = 0; i < 3; i++) {
        printf("%s is in position %d \n", zoo[i], i);
    }

    // Print dynamic array's last element
    printf("%s is in the last position %d \n", zoo[capacity - 1], capacity - 1);

    return 0;
}

// Sample Output

// Enter a capacity, greater than 4, for the dynamic zoo: 9
// Monkey is in position 0 
// Tiger is in position 1 
// Gorilla is in position 2 
// Komodo Dragon is in the last position 8 