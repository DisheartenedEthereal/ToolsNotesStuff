#include <stdio.h> 
#include <stdlib.h>
int main() 
{ 
    int age = 30;
    double gpa = 3.4;
    char grade = 'A';


    printf("Age: %p\nGPA: %p\nGrade: %p", &age ,&gpa ,&grade);
    return 0; 
} 