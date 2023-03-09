

#include <stdio.h>

// Declare and initialize global variables 
// If the global variables are decalared with the keyword const, they will not be able to be reassigned throughout the program, therefore the whatPercentage() function will return the same value on both invokations.
// const int a = 10;
int a = 10;
// const int b = 20;
int b = 20;

// whatPercentage() will return the float value of (a/b) * 100
float whatPercentage() {
    float percentage = ((float) a / (float) b) * 100;    
    return percentage;
}

// main method will first print the value of whatPercentage() with the initalized global variables. The global variables will then be updated and whatPercentage() will be called again.
int main(void) {
    printf("%d is %.2f%% of %d\n", a, whatPercentage(), b);
    printf("\n");
        
    printf("Hello NeoVim");

    a = 30;
    b = 80;

    printf("%d is %.2f%% of %d\n", a, whatPercentage(), b); 

    return 0;
}
