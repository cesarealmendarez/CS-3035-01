/*
    Cesar Almendarez
    CSULA Spring 2023
    CS 3035-01 Programming Paradigms
    Lab 18 (Structs and Pointers)
    March 23 2023
*/

#include <stdio.h>
#include <stdlib.h>

// Student struct holds their name, age, gpa
struct Student {
    char name[10];
    int age;
    float gpa;
};

// Loop & print through Student struct with pointer * 
void outputStudents(struct Student* students, int studentsCount) {
    printf("\n--- Student Records ---\n");

    for(int i = 0; i < studentsCount; i++) {
        printf("Name - %s", students[i].name);
        printf("Age - %d\n", students[i].age);
        printf("GPA -  %.2f\n\n", students[i].gpa);
    }   
}

int main() {
    // Initialize Student struct
    struct Student students[2];

    int studentsCount = 2;

    // Prompt user input for studentsCount
    for(int i = 0; i < studentsCount; i++) {
        printf("Enter student %d name: ", i + 1);
        fgets(students[i].name, 10, stdin);
        
        printf("Enter student %d age: ", i + 1);
        scanf("%d", &students[i].age);

        getchar();
        
        printf("Enter student %d GPA: ", i + 1);
        scanf("%f", &students[i].gpa);

        getchar();
    }

    outputStudents(students, studentsCount);

    return 0;
}

/*
    ---- Output ----

    Enter student 1 name: Cesar
    Enter student 1 age: 19
    Enter student 1 GPA: 4.0
    Enter student 2 name: Rasec
    Enter student 2 age: 91
    Enter student 2 GPA: 0.4

    --- Student Records ---
    Name - Cesar
    Age - 19
    GPA -  4.00

    Name - Rasec
    Age - 91
    GPA -  0.40

*/