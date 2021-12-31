#include <stdio.h> 
#include <stdlib.h>
#include <string.h>

struct Student{
    char name[50];
    char major[50];
    int age;
    double GPA;

};
int main() 
{   
    struct Student st1;
    st1.age = 22;
    st1.GPA = 3.2;
    strcpy(st1.name, "Mamdali abbas");
    strcpy(st1.major, "Khayemali");




    printf("Hello World!\n"); 
    printf("%s \n",st1.major);
    return 0; 
} 